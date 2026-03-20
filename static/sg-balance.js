// SGポイント残高を取得して表示（JWT認証版）
async function updateSGBalance() {
  try {
    const token = localStorage.getItem('access_token');
    if (!token) return;

    const response = await fetch('/api/sg/balance-jwt', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    const data = await response.json();

    if (data.success) {
      const balanceElement = document.getElementById('sgBalance');
      if (balanceElement) {
        const oldBalance = parseInt(balanceElement.textContent) || 0;
        const newBalance = data.balance;
        balanceElement.textContent = newBalance;

        // localStorageも更新
        const user = JSON.parse(localStorage.getItem('user') || '{}');
        user.sg_points = newBalance;
        localStorage.setItem('user', JSON.stringify(user));

        if (newBalance > oldBalance) {
          balanceElement.classList.add('sg-increase');
          setTimeout(() => balanceElement.classList.remove('sg-increase'), 1000);
        }
      }
    }
  } catch (error) {
    console.error('SG balance error:', error);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  updateSGBalance();
  setInterval(updateSGBalance, 30000);
});