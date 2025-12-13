// 上級モード用JavaScript（右パネル対応版）
let highQuestions = [];
let currentIndex = 0;
let correctCount = 0;
let currentScore = 0;
let answered = false;
let selectedAnswer = null;
let startTime = null;
let timerInterval = null;

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

function startChallenge() {
  const lang = document.getElementById("language").value;
  
  fetch("/api/practice/high?lang=" + encodeURIComponent(lang))
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
      
      highQuestions = data;
      currentIndex = 0;
      correctCount = 0;
      currentScore = 0;
      
      // セットアップエリアを非表示
      const setupArea = document.getElementById("setupArea");
      if (setupArea) {
        setupArea.style.display = "none";
      }
      
      // サイドパネル表示
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
      
      // 問題リスト生成
      generateQuestionList();
      
      // 最初の問題を表示
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
    
    // 問題文の最初の30文字
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
  
  // 現在の問題をハイライト
  document.querySelectorAll(".question-item").forEach((item, i) => {
    if (i === index) {
      item.classList.add("current");
    } else {
      item.classList.remove("current");
    }
  });
  
  // 進捗更新（安全にチェック）
  const currentQuestionNumberEl = document.getElementById("currentQuestionNumber");
  if (currentQuestionNumberEl) {
    currentQuestionNumberEl.textContent = index + 1;
  }
  
  const accuracy = currentIndex === 0 ? 0 : Math.round((correctCount / currentIndex) * 100);
  const accuracyRateEl = document.getElementById("accuracyRate");
  if (accuracyRateEl) {
    accuracyRateEl.textContent = accuracy + "%";
  }
  
  // 問題表示
  const questionAreaEl = document.getElementById("questionArea");
  if (questionAreaEl) {
    questionAreaEl.style.display = "block";
  }
  
  const questionTextEl = document.getElementById("questionText");
  if (questionTextEl) {
    questionTextEl.textContent = question.question;
  }
  
  const choicesArea = document.getElementById("choicesArea");
  if (choicesArea) {
    choicesArea.innerHTML = "";
    
    question.options.forEach(function(option, idx) {
      const button = document.createElement("button");
      button.innerHTML = escapeHtml(option.id + ". " + option.text);
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
  
  if (isCorrect) {
    correctCount++;
    currentScore += question.score || 1;
  }
  
  // 問題リストに結果を反映
  markQuestionResult(currentIndex, isCorrect);
  
  // ボタンの色変更
  const buttons = document.querySelectorAll("#choicesArea button");
  buttons.forEach(function(btn, idx) {
    btn.disabled = true;
    if (idx === correctIndex) {
      btn.classList.add("correct");
    } else if (idx === selectedIndex && !isCorrect) {
      btn.classList.add("incorrect");
    }
  });
  
  // フィードバック表示
  const feedbackArea = document.getElementById("feedbackArea");
  feedbackArea.style.display = "block";
  
  if (isCorrect) {
    feedbackArea.className = "feedback correct";
    feedbackArea.innerHTML = "<h3>✓ 正解！</h3><p>+" + (question.score || 1) + "点</p>";
  } else {
    const correctOption = question.options[correctIndex];
    feedbackArea.className = "feedback incorrect";
    feedbackArea.innerHTML = "<h3>✗ 不正解</h3><p>正解は <strong>" + escapeHtml(correctOption.id + ". " + correctOption.text) + "</strong> です</p>";
  }
  
  // 解説表示
  const explanationArea = document.getElementById("explanationArea");
  explanationArea.style.display = "block";
  document.getElementById("explanationText").textContent = question.explanation || "解説はありません";
  document.getElementById("learningPointText").textContent = question.learning_point || "学習ポイントはありません";
  
  document.getElementById("nextButtonArea").style.display = "block";
  
  // 進捗更新
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
    // 既に解答済みの問題は見直しのみ
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