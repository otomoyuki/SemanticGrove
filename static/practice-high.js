// 上級モード用JavaScript（正しい選択肢シャッフル実装）
let highQuestions = [];
let currentIndex = 0;
let correctCount = 0;
let currentScore = 0;
let answered = false;
let selectedAnswer = null;
let startTime = null;
let timerInterval = null;
let selectedLanguage = '';

// HTMLエスケープ関数
function escapeHtml(text) {
  const map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  };
  return text.replace(/[&<>"']/g, m => map[m]);
}

// 選択肢の中身だけをシャッフルする関数
function shuffleOptions(question) {
  const originalOptions = [...question.options];
  const originalCorrectIndex = question.answer[0];
  
  const labels = ['A', 'B', 'C', 'D'];
  const indices = originalOptions.map((_, index) => index);
  
  // Fisher-Yates シャッフル
  for (let i = indices.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [indices[i], indices[j]] = [indices[j], indices[i]];
  }
  
  // ラベルは固定、中身だけシャッフル
  const shuffledOptions = indices.map((originalIndex, newIndex) => ({
    id: labels[newIndex],
    text: originalOptions[originalIndex].text
  }));
  
  const newCorrectIndex = indices.indexOf(originalCorrectIndex);
  
  return {
    ...question,
    options: shuffledOptions,
    answer: [newCorrectIndex],
    originalOptions: originalOptions,
    originalAnswer: [originalCorrectIndex]
  };
}

function startChallenge() {
  const lang = document.getElementById("language").value;
  selectedLanguage = lang;
  const questionCount = document.getElementById("questionCount") ? 
    document.getElementById("questionCount").value : "10";
  
  fetch("/api/practice/high?lang=" + encodeURIComponent(lang) + "&limit=" + questionCount)
    .then(function(res) {
      if (!res.ok) throw new Error("HTTP error! status: " + res.status);
      return res.json();
    })
    .then(function(data) {
      if (data.length === 0) {
        alert("選択した言語の問題がありません");
        location.reload();
        return;
      }
      
      // 各問題の選択肢をシャッフル
      highQuestions = data.map(q => shuffleOptions(q));
      
      currentIndex = 0;
      correctCount = 0;
      currentScore = 0;
      
      const setupArea = document.getElementById("setupArea");
      if (setupArea) {
        setupArea.style.display = "none";
      }
      
      const sidePanel = document.getElementById("sidePanel");
      if (sidePanel) {
        sidePanel.style.display = "block";
      }
      
      const panelLanguage = document.getElementById("panelLanguage");
      if (panelLanguage) {
        panelLanguage.textContent = lang;
      }
      
      const totalQuestions = document.getElementById("totalQuestions");
      if (totalQuestions) {
        totalQuestions.textContent = highQuestions.length;
      }
      
      generateQuestionList();
      showQuestion(0);
      startTimer();
    })
    .catch(function(error) {
      console.error("Error:", error);
      alert("問題の読み込みに失敗しました: " + error.message);
    });
}

function generateQuestionList() {
  const listContainer = document.getElementById("questionList");
  listContainer.innerHTML = "";
  
  highQuestions.forEach((q, index) => {
    const item = document.createElement("div");
    item.className = "question-item";
    item.id = `q-item-${index}`;
    
    const shortText = q.question.substring(0, 30) + (q.question.length > 30 ? "..." : "");
    
    item.innerHTML = `
      <div class="q-number">${index + 1}</div>
      <div class="q-content">
        <div class="q-text">${escapeHtml(shortText)}</div>
        <div class="q-stats">
          <span>難易度: ${q.difficulty || '中'}</span>
          <span>${q.score || 1}pt</span>
        </div>
      </div>
      <div class="q-achievement"></div>
    `;
    
    item.onclick = () => jumpToQuestion(index);
    listContainer.appendChild(item);
  });
}

function showQuestion(index) {
  currentIndex = index;
  answered = false;
  selectedAnswer = null;
  
  const question = highQuestions[currentIndex];
  
  document.querySelectorAll(".question-item").forEach((item, i) => {
    if (i === index) {
      item.classList.add("current");
    } else {
      item.classList.remove("current");
    }
  });
  
  const currentQuestionNumberEl = document.getElementById("currentQuestionNumber");
  if (currentQuestionNumberEl) {
    currentQuestionNumberEl.textContent = index + 1;
  }
  
  const accuracy = currentIndex === 0 ? 0 : Math.round((correctCount / currentIndex) * 100);
  const accuracyRateEl = document.getElementById("accuracyRate");
  if (accuracyRateEl) {
    accuracyRateEl.textContent = accuracy + "%";
  }
  
  const questionAreaEl = document.getElementById("questionArea");
  if (questionAreaEl) {
    questionAreaEl.style.display = "block";
  }
  
  const questionTextEl = document.getElementById("questionText");
  if (questionTextEl) {
    if (question.image) {
      const imagePath = question.image.replace(/^images\//, '');
      const fullPath = `/static/images/${imagePath}`;
      console.log("=== 画像情報 ===");
      console.log("元のパス:", question.image);
      console.log("修正後のパス:", imagePath);
      console.log("完全なURL:", fullPath);
      
      questionTextEl.innerHTML = `
        <img src="${fullPath}" 
             alt="問題画像" 
             style="max-width: 600px; width: 100%; height: auto; margin: 20px 0; display: block; border: 2px solid #4a7c59; border-radius: 8px;"
             onerror="console.error('❌ 画像読み込み失敗:', '${fullPath}'); this.style.display='none'; this.insertAdjacentHTML('afterend', '<p style=\\'color:red; font-weight:bold;\\'>画像を読み込めませんでした: ${imagePath}</p>');"
             onload="console.log('✅ 画像読み込み成功:', '${fullPath}')">
        <p style="margin-top: 10px;">${escapeHtml(question.question)}</p>
      `;
    } else {
      questionTextEl.textContent = question.question;
    }
  }
  
  const choicesArea = document.getElementById("choicesArea");
  if (choicesArea) {
    choicesArea.innerHTML = "";
    
    question.options.forEach(function(option, idx) {
      const button = document.createElement("button");
      button.innerHTML = escapeHtml(option.text);  // ラベル削除
      button.onclick = function() { selectAnswer(idx); };
      button.id = "option-" + idx;
      choicesArea.appendChild(button);
    });
  }
  
  const feedbackArea = document.getElementById("feedbackArea");
  if (feedbackArea) feedbackArea.style.display = "none";
  
  const explanationArea = document.getElementById("explanationArea");
  if (explanationArea) explanationArea.style.display = "none";
  
  const nextButtonArea = document.getElementById("nextButtonArea");
  if (nextButtonArea) nextButtonArea.style.display = "none";
}

function selectAnswer(selectedIndex) {
  if (answered) return;
  
  answered = true;
  selectedAnswer = selectedIndex;
  
  const question = highQuestions[currentIndex];
  const correctIndex = question.answer[0];
  const isCorrect = selectedIndex === correctIndex;
  
  recordAnswer(question.id, isCorrect, question);

  if (isCorrect) {
    correctCount++;
    currentScore += question.score || 1;
  }
  
  markQuestionResult(currentIndex, isCorrect);
  
  const buttons = document.querySelectorAll("#choicesArea button");
  buttons.forEach(function(btn, idx) {
    btn.disabled = true;
    if (idx === correctIndex) {
      btn.classList.add("correct");
    } else if (idx === selectedIndex && !isCorrect) {
      btn.classList.add("incorrect");
    }
  });
  
  const feedbackArea = document.getElementById("feedbackArea");
  feedbackArea.style.display = "block";
  
  if (isCorrect) {
    feedbackArea.className = "feedback correct";
    feedbackArea.innerHTML = "<h3>✓ 正解！</h3><p>+" + (question.score || 1) + "点</p>";
  } else {
    const correctOption = question.options[correctIndex];
    feedbackArea.className = "feedback incorrect";
    feedbackArea.innerHTML = "<h3>✗ 不正解</h3><p>正解は <strong>" + escapeHtml(correctOption.text) + "</strong> です</p>";  // ラベル削除
  }
  
  const explanationArea = document.getElementById("explanationArea");
  explanationArea.style.display = "block";
  document.getElementById("explanationText").textContent = question.explanation || "解説はありません";
  document.getElementById("learningPointText").textContent = question.learning_point || "学習ポイントはありません";
  
  document.getElementById("nextButtonArea").style.display = "block";
  
  const accuracy = Math.round((correctCount / (currentIndex + 1)) * 100);
  document.getElementById("accuracyRate").textContent = accuracy + "%";
}

function markQuestionResult(index, isCorrect) {
  const item = document.getElementById(`q-item-${index}`);
  
  if (isCorrect) {
    item.classList.add("correct");
    item.querySelector(".q-achievement").textContent = "✓";
  } else {
    item.classList.add("incorrect");
    item.querySelector(".q-achievement").textContent = "✗";
  }
}

function jumpToQuestion(index) {
  if (index < currentIndex) {
    alert("この問題は既に解答済みです");
    return;
  }
  showQuestion(index);
}

function goNextHigh() {
  currentIndex++;
  
  if (currentIndex < highQuestions.length) {
    showQuestion(currentIndex);
  } else {
    showHighResult();
  }
}

function startTimer() {
  startTime = Date.now();
  timerInterval = setInterval(updateTimer, 1000);
}

function updateTimer() {
  const elapsed = Math.floor((Date.now() - startTime) / 1000);
  const minutes = Math.floor(elapsed / 60);
  const seconds = elapsed % 60;
  const timerDisplay = document.getElementById("timerDisplay");
  if (timerDisplay) {
    timerDisplay.textContent = 
      String(minutes).padStart(2, "0") + ":" + String(seconds).padStart(2, "0");
  }
}

function stopTimer() {
  if (timerInterval) {
    clearInterval(timerInterval);
    timerInterval = null;
  }
}

function getElapsedTime() {
  if (!startTime) return 0;
  return Math.floor((Date.now() - startTime) / 1000);
}

function showHighResult() {
  stopTimer();
  const elapsedTime = getElapsedTime();
  
  document.getElementById("questionArea").style.display = "none";
  document.getElementById("sidePanel").style.display = "none";
  
  const total = highQuestions.length;
  const incorrect = total - correctCount;
  const accuracy = Math.round((correctCount / total) * 100);
  
  const minutes = Math.floor(elapsedTime / 60);
  const seconds = elapsedTime % 60;
  const timeDisplay = String(minutes).padStart(2, "0") + ":" + String(seconds).padStart(2, "0");
  
  document.getElementById("finalTotal").textContent = total;
  document.getElementById("finalCorrect").textContent = correctCount;
  document.getElementById("finalIncorrect").textContent = incorrect;
  document.getElementById("finalAccuracy").textContent = accuracy;
  document.getElementById("finalTime").textContent = timeDisplay;
  document.getElementById("finalScore").textContent = currentScore;
  
  const rankingMessage = document.getElementById("rankingMessage");
  if (rankingMessage) {
    if (accuracy >= 80) {
      rankingMessage.innerHTML = "🎉 素晴らしい成績です！ランキング上位を狙えます！";
    } else if (accuracy >= 60) {
      rankingMessage.innerHTML = "👍 良い結果です！もう一度挑戦してみましょう！";
    } else {
      rankingMessage.innerHTML = "💪 学習モードで復習してから再挑戦しましょう！";
    }
  }
  
  saveScore(currentScore, elapsedTime, correctCount, total);
  
  document.getElementById("resultArea").style.display = "block";
}

function saveScore(score, time, correct, total) {
  fetch("/api/save-score", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      mode: "high",
      language: document.getElementById("language") ? document.getElementById("language").value : "すべて",
      score: score,
      time: time,
      correct: correct,
      total: total
    })
  })
  .then(function(res) { return res.json(); })
  .then(function(data) {
    if (data.success) {
      console.log("Score saved successfully!");
    } else {
      console.log("Not logged in or error saving score");
    }
  })
  .catch(function(error) {
    console.log("Error saving score:", error);
  });
}

function viewRanking() {
  alert("ランキング機能は実装予定です");
}

function restartHigh() {
  location.reload();
}

// ==================== SGポイント連携 ====================

// 回答を記録してSGポイントを付与
// ✅ 第3引数を追加
async function recordAnswer(questionId, isCorrect, question) {
  try {
    const language = selectedLanguage || 'Unknown';
    const mode = getModeFromPage();
    
    const response = await fetch('/api/answer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        question_id: questionId,
        language: language,
        category: question.category || '',      // ← questionから取得
        difficulty: question.difficulty || '1', // ← questionから取得
        mode: mode,
        is_correct: isCorrect
      })
    });
    
    if (response.ok && isCorrect) {
      // SGポイント表示を更新
      if (typeof updateSGBalance === 'function') {
        setTimeout(() => updateSGBalance(), 500);
      }
    }
  } catch (error) {
    console.error('Answer recording error:', error);
  }
}
function getModeFromPage() {
  const path = window.location.pathname;
  if (path.includes('/low')) return 'beginner';
  if (path.includes('/middle')) return 'intermediate';
  if (path.includes('/high')) return 'advanced';
  return 'practice';
}