// 中級モード用JavaScript
let middleQuestions = [];
let currentIndex = 0;
let correctCount = 0;
let answered = false;
let selectedAnswer = null;

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

function startMiddleMode() {
  const lang = document.getElementById("language").value;
  document.getElementById("setupArea").innerHTML = "<p>問題を読み込み中...</p>";
  
  fetch("/api/practice/middle?lang=" + encodeURIComponent(lang))
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
      
      middleQuestions = data;
      currentIndex = 0;
      correctCount = 0;
      
      document.getElementById("setupArea").style.display = "none";
      document.getElementById("scoreDisplay").style.display = "block";
      document.getElementById("questionArea").style.display = "block";
      
      document.getElementById("totalQuestions").textContent = middleQuestions.length;
      
      showMiddleQuestion();
    })
    .catch(function(error) {
      console.error("Error:", error);
      alert("問題の読み込みに失敗しました: " + error.message);
      location.reload();
    });
}

function showMiddleQuestion() {
  const question = middleQuestions[currentIndex];
  answered = false;
  selectedAnswer = null;
  
  document.getElementById("currentQuestion").textContent = currentIndex + 1;
  document.getElementById("correctCount").textContent = correctCount;
  const accuracy = currentIndex === 0 ? 0 : Math.round((correctCount / currentIndex) * 100);
  document.getElementById("accuracyRate").textContent = accuracy;
  
  document.getElementById("questionText").textContent = question.question;
  
  const choicesArea = document.getElementById("choicesArea");
  choicesArea.innerHTML = "";
  
  question.options.forEach(function(option, index) {
    const button = document.createElement("button");
    button.innerHTML = escapeHtml(option.id + ". " + option.text);
    button.onclick = function() { selectAnswer(index); };
    button.id = "option-" + index;
    choicesArea.appendChild(button);
  });
  
  document.getElementById("feedbackArea").style.display = "none";
  document.getElementById("explanationArea").style.display = "none";
  document.getElementById("nextButtonArea").style.display = "none";
}

function selectAnswer(selectedIndex) {
  if (answered) return;
  
  answered = true;
  selectedAnswer = selectedIndex;
  
  const question = middleQuestions[currentIndex];
  const correctIndex = question.answer[0];
  const isCorrect = selectedIndex === correctIndex;
  
  if (isCorrect) {
    correctCount++;
  }
  
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
    feedbackArea.innerHTML = "<h3>✓ 正解！</h3><p>+" + question.score + "点</p>";
  } else {
    const correctOption = question.options[correctIndex];
    feedbackArea.className = "feedback incorrect";
    feedbackArea.innerHTML = "<h3>✗ 不正解</h3><p>正解は <strong>" + escapeHtml(correctOption.id + ". " + correctOption.text) + "</strong> です</p>";
  }
  
  const explanationArea = document.getElementById("explanationArea");
  explanationArea.style.display = "block";
  document.getElementById("explanationText").textContent = question.explanation || "解説はありません";
  document.getElementById("learningPointText").textContent = question.learning_point || "学習ポイントはありません";
  
  document.getElementById("nextButtonArea").style.display = "block";
  
  document.getElementById("correctCount").textContent = correctCount;
  const accuracy = Math.round((correctCount / (currentIndex + 1)) * 100);
  document.getElementById("accuracyRate").textContent = accuracy;
}

function goNextMiddle() {
  currentIndex++;
  
  if (currentIndex < middleQuestions.length) {
    showMiddleQuestion();
  } else {
    showMiddleResult();
  }
}

function showMiddleResult() {
  document.getElementById("scoreDisplay").style.display = "none";
  document.getElementById("questionArea").style.display = "none";
  document.getElementById("feedbackArea").style.display = "none";
  document.getElementById("explanationArea").style.display = "none";
  document.getElementById("nextButtonArea").style.display = "none";
  
  const total = middleQuestions.length;
  const incorrect = total - correctCount;
  const accuracy = Math.round((correctCount / total) * 100);
  
  const avgScore = middleQuestions.reduce(function(sum, q) {
    return sum + (q.score || 1);
  }, 0) / total;
  const finalScore = Math.round(correctCount * avgScore);
  
  document.getElementById("finalTotal").textContent = total;
  document.getElementById("finalCorrect").textContent = correctCount;
  document.getElementById("finalIncorrect").textContent = incorrect;
  document.getElementById("finalAccuracy").textContent = accuracy;
  document.getElementById("finalScore").textContent = finalScore;
  
  document.getElementById("resultArea").style.display = "block";
}

function restartMiddle() {
  location.reload();
}