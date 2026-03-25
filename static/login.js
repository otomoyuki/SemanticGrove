// static/login.js
// JWT認証統合版

document.addEventListener('DOMContentLoaded', async function() {
    console.log('✅ Login page loaded');

    // DOM要素（DOMContentLoaded内で取得するので確実にnullにならない）
    const form = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const submitBtn = document.getElementById('submitBtn');
    const errorMessage = document.getElementById('errorMessage');
    const successMessage = document.getElementById('successMessage');

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

    // パスワード表示切替
    document.getElementById('togglePassword')?.addEventListener('click', function() {
        const type = passwordInput.type === 'password' ? 'text' : 'password';
        passwordInput.type = type;
        this.textContent = type === 'password' ? '👁️' : '🙈';
    });

    // 既にログイン済みの場合はトークンを検証してからリダイレクト
    const token = localStorage.getItem('access_token');
    if (token) {
        try {
            const res = await fetch('/api/sg/balance-jwt', {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            if (res.ok) {
                console.log('Already logged in, redirecting...');
                window.location.href = '/';
                return;
            } else {
                console.log('Token invalid, clearing...');
                localStorage.clear();
            }
        } catch (e) {
            localStorage.clear();
        }
    }

    // ログアウト後のメッセージ
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('logout') === 'success') {
        showSuccess('ログアウトしました');
    }

    // フォーム送信
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // メッセージをリセット
        errorMessage.style.display = 'none';
        successMessage.style.display = 'none';

        const username = usernameInput.value.trim();
        const password = passwordInput.value;

        if (!username || !password) {
            showError('ユーザー名とパスワードを入力してください');
            return;
        }

        submitBtn.disabled = true;
        submitBtn.textContent = 'ログイン中...';

        try {
            const response = await fetch('/api/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (data.success) {
                localStorage.setItem('access_token', data.access_token);
                localStorage.setItem('refresh_token', data.refresh_token);
                localStorage.setItem('user', JSON.stringify(data.user));

                let message = `ログイン成功！ようこそ ${data.user.username} さん`;
                if (data.login_bonus > 0) {
                    message += `\n🎁 ログインボーナス: +${data.login_bonus} SG`;
                }
                showSuccess(message);

                setTimeout(() => {
                    const redirect = new URLSearchParams(window.location.search).get('redirect') || '/';
                    window.location.href = redirect;
                }, 1500);

            } else {
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
});