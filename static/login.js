// static/login.js
// JWT認証統合版

// DOM要素
const form = document.getElementById('loginForm');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const submitBtn = document.getElementById('submitBtn');
const errorMessage = document.getElementById('errorMessage');
const successMessage = document.getElementById('successMessage');

// パスワード表示切替
document.getElementById('togglePassword')?.addEventListener('click', function() {
    const type = passwordInput.type === 'password' ? 'text' : 'password';
    passwordInput.type = type;
    this.textContent = type === 'password' ? '👁️' : '🙈';
});

// フォーム送信
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // メッセージをリセット
    errorMessage.style.display = 'none';
    successMessage.style.display = 'none';
    
    // フォームデータ取得
    const username = usernameInput.value.trim();
    const password = passwordInput.value;
    
    // バリデーション
    if (!username || !password) {
        showError('ユーザー名とパスワードを入力してください');
        return;
    }
    
    // ボタンを無効化
    submitBtn.disabled = true;
    submitBtn.textContent = 'ログイン中...';
    
    try {
        // JWT認証API呼び出し
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // トークンをlocalStorageに保存
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);
            localStorage.setItem('user', JSON.stringify(data.user));
            
            // 成功メッセージ
            let message = `ログイン成功！ようこそ ${data.user.username} さん`;
            if (data.login_bonus > 0) {
                message += `\n🎁 ログインボーナス: +${data.login_bonus} SG`;
            }
            showSuccess(message);
            
            // リダイレクト
            setTimeout(() => {
                // URLパラメータにredirectがあればそちらへ
                const urlParams = new URLSearchParams(window.location.search);
                const redirect = urlParams.get('redirect') || '/';
                window.location.href = redirect;
            }, 1500);
            
        } else {
            // ログイン失敗時にlocalStorageをクリア（古いトークン除去）
            localStorage.clear();
            showError(data.error || 'ログインに失敗しました');
            submitBtn.disabled = false;
            submitBtn.textContent = '🔐 ログイン';
}

    } catch (error) {
        console.error('Login error:', error);
        showError('ログインに失敗しました。もう一度お試しください。');
        submitBtn.disabled = false;
        submitBtn.textContent = '🔐 ログイン';
    }
});

// エラーメッセージ表示
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// 成功メッセージ表示
function showSuccess(message) {
    successMessage.textContent = message;
    successMessage.style.display = 'block';
    successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// ページ読み込み時
document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ Login page loaded');
    
    // 既にログイン済みの場合はリダイレクト
    const token = localStorage.getItem('access_token');
    if (token) {
        console.log('Already logged in, redirecting...');
        window.location.href = '/';
    }
    
    // ログアウト後のメッセージ
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('logout') === 'success') {
        showSuccess('ログアウトしました');
    }
});