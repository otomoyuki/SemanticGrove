// ============================================================
// 学習モード専用JavaScript（画像対応版）
// ============================================================
let learnQuestions = [];
let learnIndex = 0;

// ページ読み込み時に実行（学習モードページの場合のみ）
window.onload = function() {
  // 言語選択要素が存在する場合のみ実行
  const languageSelect = document.getElementById("language");
  if (languageSelect) {
    startLearning();
  }
};

// 言語選択時に学習データを取得
function startLearning() {
  const langElement = document.getElementById("language");
  if (!langElement) return; // 要素がなければ終了
  
  const lang = langElement.value;
  const learningBox = document.querySelector(".learning-box");
  
  if (!learningBox) return; // 要素がなければ終了
  
  // ローディング表示
  learningBox.innerHTML = `<p>読み込み中...</p>`;
  
  // APIから問題を取得
  fetch(`/api/learn?lang=${encodeURIComponent(lang)}`)
    .then(res => {
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      return res.json();
    })
    .then(data => {
      learnQuestions = data;
      learnIndex = 0;
      
      if (data.length === 0) {
        learningBox.innerHTML = `<p>選択した言語の問題がありません</p>`;
        return;
      }
      
      showLearningQuestion();
    })
    .catch(error => {
      console.error('Error:', error);
      learningBox.innerHTML = `<p>エラーが発生しました: ${error.message}</p>`;
    });
}

// 学習問題を表示（画像対応版）
function showLearningQuestion() {
  const data = learnQuestions[learnIndex];
  if (!data) return;
  
  const learningBox = document.querySelector(".learning-box");
  if (!learningBox) return;
  
  // answerは配列で、[2]のような形式
  // optionsは [{"id":"A","text":"赤"}, ...] の配列
  const correctIndex = data.answer[0]; // 例: 2
  const correctOption = data.options[correctIndex];
  const correctText = correctOption ? correctOption.text : "不明";
  
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
  
  // 画像があるかチェック
  const hasImage = data.image && data.image.trim() !== '';
  
  // 画像HTML（ある場合のみ）
  const imageHtml = hasImage ? `
    <div style="text-align: center; margin: 20px 0;">
      <img src="/static/${data.image}" 
           alt="問題図" 
           style="max-width: 100%; height: auto; border: 2px solid #4a9eff; border-radius: 8px;"
           onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
      <p style="display: none; color: #ff6b6b;">画像の読み込みに失敗しました: ${escapeHtml(data.image)}</p>
    </div>
  ` : '';
  
  learningBox.innerHTML = `
    <h2>問題 ${learnIndex + 1} / ${learnQuestions.length}</h2>
    <p><strong>${escapeHtml(data.question)}</strong></p>
    
    ${imageHtml}
    
    <h3>選択肢：</h3>
    <ul>
      ${data.options.map((opt, idx) => `
        <li style="color: ${idx === correctIndex ? 'green' : '#f0f0f0'}; font-weight: ${idx === correctIndex ? 'bold' : 'normal'};">
          ${opt.id}. ${escapeHtml(opt.text)} ${idx === correctIndex ? '✓' : ''}
        </li>
      `).join('')}
    </ul>
    
    <h3>正解：</h3>
    <p style="color: #4f4; font-weight: bold;">${correctOption.id}. ${escapeHtml(correctText)}</p>
    
    <h3>解説：</h3>
    <p>${escapeHtml(data.explanation)}</p>
    
    <h3>学習ポイント：</h3>
    <p>${escapeHtml(data.learning_point || 'なし')}</p>
  `;
}

// 次の問題へ
function goNext() {
  learnIndex++;
  if (learnIndex < learnQuestions.length) {
    showLearningQuestion();
  } else {
    const learningBox = document.querySelector(".learning-box");
    if (learningBox) {
      learningBox.innerHTML = `
        <h2>お疲れ様でした！</h2>
        <p>学習コンテンツは終了しました。</p>
        <p>全${learnQuestions.length}問を学習しました。</p>
        <button onclick="startLearning()">最初から復習する</button>
      `;
    }
  }
}

// ホームへ戻る
function goHome() {
  window.location.href = "/";
}

// READMEを開く
function openReadme() {
  window.open("/readme", "_blank");
}