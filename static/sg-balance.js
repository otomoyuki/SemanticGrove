// SGポイント残高を取得して表示
async function updateSGBalance() {
  try {
    const response = await fetch('/api/sg/balance');
    const data = await response.json();
    
    if (data.success) {
      // 残高を更新
      const balanceElement = document.getElementById('sgBalance');
      if (balanceElement) {
        const oldBalance = parseInt(balanceElement.textContent) || 0;
        const newBalance = data.balance;
        
        balanceElement.textContent = newBalance;
        
        // ボーナスがあればアニメーション
        if (data.bonus > 0) {
          showSGBonus(data.bonus);
        }
        
        // 増加があればアニメーション
        if (newBalance > oldBalance) {
          balanceElement.classList.add('sg-increase');
          setTimeout(() => {
            balanceElement.classList.remove('sg-increase');
          }, 1000);
        }
      }
    }
  } catch (error) {
    console.error('SG balance error:', error);
  }
}

// ボーナス獲得メッセージを表示
function showSGBonus(amount) {
  const message = document.createElement('div');
  message.className = 'sg-bonus-message';
  message.textContent = `+${amount} SG 獲得！`;
  document.body.appendChild(message);
  
  setTimeout(() => {
    message.classList.add('show');
  }, 100);
  
  setTimeout(() => {
    message.classList.remove('show');
    setTimeout(() => message.remove(), 500);
  }, 3000);
}

// ページ読み込み時に実行
document.addEventListener('DOMContentLoaded', () => {
  updateSGBalance();
  
  // 30秒ごとに更新（練習中にリアルタイム反映）
  setInterval(updateSGBalance, 30000);
});