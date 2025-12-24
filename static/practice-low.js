// 初級モード用JavaScript（正しい選択肢シャッフル実装）
let lowQuestions = [];
let currentIndex = 0;
let correctCount = 0;
let answered = false;
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
  // 元の選択肢を保存
  const originalOptions = [...question.options];
  const originalCorrectIndex = question.answer[0];
  
  // 固定ラベル（A, B, C, Dは変えない）
  const labels = ['A', 'B', 'C', 'D'];
  
  // インデックスの配列を作成 [0, 1, 2, 3]
  const indices = originalOptions.map((_, index) => index);
  
  // Fisher-Yates シャッフル
  for (let i = indices.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [indices[i], indices[j]] = [indices[j], indices[i]];
  }
  
  // シャッフルした選択肢を作成（ラベルは固定、中身だけシャッフル）
  const shuffledOptions = indices.map((originalIndex, newIndex) => ({
    id: labels[newIndex],  // ラベルは常にA, B, C, D
    text: originalOptions[originalIndex].text  // 中身だけシャッフル
  }));
  
  // 新しい正解インデックスを見つける
  const newCorrectIndex = indices.indexOf(originalCorrectIndex);
  
  return {
    ...question,
    options: shuffledOptions,
    answer: [newCorrectIndex],
    originalOptions: originalOptions,
    originalAnswer: [originalCorrectIndex]
  };
}

function startLowMode() {
  const lang = document.getElementById("language").value;
  selectedLanguage = lang; 
  const questionCount = document.getElementById("questionCount") ? 
    document.getElementById("questionCount").value : "10";
  
  document.getElementById("setupArea").innerHTML = "<p>問題を読み込み中...</p>";
  
  fetch("/api/practice/low?lang=" + encodeURIComponent(lang) + "&limit=" + questionCount)
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
      lowQuestions = data.map(q => shuffleOptions(q));
      
      console.log("シャッフル後の最初の問題:", lowQuestions[0]);
      
      currentIndex = 0;
      correctCount = 0;
      
      document.getElementById("setupArea").style.display = "none";
      document.getElementById("scoreDisplay").style.display = "block";
      document.getElementById("questionArea").style.display = "block";
      
      document.getElementById("totalQuestions").textContent = lowQuestions.length;
      
      showLowQuestion();
    })
    .catch(function(error) {
      console.error("Error:", error);
      alert("問題の読み込みに失敗しました: " + error.message);
      location.reload();
    });
}

function showLowQuestion() {
  const question = lowQuestions[currentIndex];
  answered = false;
  
  console.log("現在の問題:", question);
  console.log("正解インデックス:", question.answer[0]);
  console.log("選択肢:", question.options);
  
  document.getElementById("currentQuestion").textContent = currentIndex + 1;
  document.getElementById("correctCount").textContent = correctCount;
  
  document.getElementById("questionNumber").textContent = currentIndex + 1;
  const questionTextElement = document.getElementById("questionText");

  if (question.image) {
    // "images/"プレフィックスを削除（重複を防ぐ）
    const imagePath = question.image.replace(/^images\//, '');
    const fullPath = `/static/images/${imagePath}`;
    console.log("=== 画像情報 ===");
    console.log("元のパス:", question.image);
    console.log("修正後のパス:", imagePath);
    console.log("完全なURL:", fullPath);
    console.log("問題ID:", currentIndex + 1);
    
    questionTextElement.innerHTML = `
      <img src="${fullPath}" 
           alt="問題画像" 
           style="max-width: 600px; width: 100%; height: auto; margin: 20px 0; display: block; border: 2px solid #4a7c59; border-radius: 8px;"
           onerror="console.error('❌ 画像読み込み失敗:', '${fullPath}'); this.style.display='none'; this.insertAdjacentHTML('afterend', '<p style=\\'color:red; font-weight:bold;\\'>画像を読み込めませんでした: ${imagePath}</p>');"
           onload="console.log('✅ 画像読み込み成功:', '${fullPath}')">
      <p style="margin-top: 10px;">${escapeHtml(question.question)}</p>
    `;
  } else {
    questionTextElement.textContent = question.question;
  } 
  
  // 選択肢をボタン形式で表示（ラベルA, B, C, D固定、中身シャッフル済み）
  const choicesArea = document.getElementById("choicesArea");
  choicesArea.innerHTML = "";
  
  question.options.forEach(function(option, index) {
    const button = document.createElement("button");
    button.innerHTML = escapeHtml(option.text);  // ラベル削除
    button.onclick = function() { selectLowAnswer(index); };
    button.id = "option-" + index;
    choicesArea.appendChild(button);
  });
  
  // 解説エリアは最初から表示
  document.getElementById("explanationArea").style.display = "block";
  document.getElementById("explanationText").textContent = question.explanation || "解説はありません";
  document.getElementById("learningPointText").textContent = question.learning_point || "学習ポイントはありません";
  
  document.getElementById("feedbackArea").style.display = "none";
  document.getElementById("nextButtonArea").style.display = "none";
}

function selectLowAnswer(selectedIndex) {
  if (answered) return;
  
  answered = true;
  
  const question = lowQuestions[currentIndex];
  const correctIndex = question.answer[0];
  const isCorrect = selectedIndex === correctIndex;

  recordAnswer(question.id, isCorrect, question);
  
  console.log("選択:", selectedIndex, "正解:", correctIndex, "結果:", isCorrect);
  
  if (isCorrect) {
    correctCount++;
  }
  
  // ボタンの色を変更
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
    feedbackArea.innerHTML = "<h3>✓ 正解！</h3><p>+" + question.score + "点</p>";
  } else {
    const correctOption = question.options[correctIndex];
    feedbackArea.className = "feedback incorrect";
    feedbackArea.innerHTML = "<h3>✗ 不正解</h3><p>正解は <strong>" + escapeHtml(correctOption.id + ". " + correctOption.text) + "</strong> です</p>";
  }
  
  document.getElementById("nextButtonArea").style.display = "block";
  document.getElementById("correctCount").textContent = correctCount;
}

function goNextLow() {
  currentIndex++;
  
  if (currentIndex < lowQuestions.length) {
    showLowQuestion();
  } else {
    showLowResult();
  }
}

function showLowResult() {
  document.getElementById("scoreDisplay").style.display = "none";
  document.getElementById("questionArea").style.display = "none";
  document.getElementById("feedbackArea").style.display = "none";
  document.getElementById("explanationArea").style.display = "none";
  document.getElementById("nextButtonArea").style.display = "none";
  
  const total = lowQuestions.length;
  const incorrect = total - correctCount;
  const accuracy = Math.round((correctCount / total) * 100);
  
  document.getElementById("finalTotal").textContent = total;
  document.getElementById("finalCorrect").textContent = correctCount;
  document.getElementById("finalIncorrect").textContent = incorrect;
  document.getElementById("finalAccuracy").textContent = accuracy;
  
  document.getElementById("resultArea").style.display = "block";
}

function restartLow() {
  location.reload();
}

// ==================== SGポイント連携 ====================

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
        category: question.category || '',
        difficulty: question.difficulty || '1',
        mode: mode,
        is_correct: isCorrect
      })
    });
    
    if (response.ok && isCorrect) {
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