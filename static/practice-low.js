// 初級モード用JavaScript（中級と同じボタン形式 + 解説表示）
let lowQuestions = [];
let currentIndex = 0;
let correctCount = 0;
let answered = false;

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

function startLowMode() {
  const lang = document.getElementById("language").value;
  document.getElementById("setupArea").innerHTML = "<p>問題を読み込み中...</p>";
  
  fetch("/api/practice/low?lang=" + encodeURIComponent(lang))
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
      
      lowQuestions = data;
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
  
  document.getElementById("currentQuestion").textContent = currentIndex + 1;
  document.getElementById("correctCount").textContent = correctCount;
  
  document.getElementById("questionNumber").textContent = currentIndex + 1;
 const questionTextElement = document.getElementById("questionText");

if (question.image) {
  questionTextElement.innerHTML = `
    <img src="/static/images/${question.image}" 
         alt="問題画像" 
         style="max-width: 600px; width: 100%; height: auto; margin: 20px 0; display: block;">
    <p style="margin-top: 10px;">${escapeHtml(question.question)}</p>
  `;
} else {
  questionTextElement.textContent = question.question;
} 
  // 選択肢をボタン形式で表示
  const choicesArea = document.getElementById("choicesArea");
  choicesArea.innerHTML = "";
  
  question.options.forEach(function(option, index) {
    const button = document.createElement("button");
    button.innerHTML = escapeHtml(option.id + ". " + option.text);
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