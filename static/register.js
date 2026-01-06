// static/register-enhanced.js
// 既存のUI機能 + JWT認証統合版

// DOM要素
const form = document.getElementById('registerForm');
const usernameInput = document.getElementById('username');
const emailInput = document.getElementById('email');
const displayNameInput = document.getElementById('displayName');
const passwordInput = document.getElementById('password');
const passwordConfirmInput = document.getElementById('passwordConfirm');
const agreeTermsCheckbox = document.getElementById('agreeTerms');
const submitBtn = document.getElementById('submitBtn');
const errorMessage = document.getElementById('errorMessage');
const successMessage = document.getElementById('successMessage');
const passwordStrength = document.getElementById('passwordStrength');
const passwordMatch = document.getElementById('passwordMatch');

// パスワード表示切替
document.getElementById('togglePassword')?.addEventListener('click', function() {
    const type = passwordInput.type === 'password' ? 'text' : 'password';
    passwordInput.type = type;
    this.textContent = type === 'password' ? '👁️' : '🙈';
});

document.getElementById('togglePasswordConfirm')?.addEventListener('click', function() {
    const type = passwordConfirmInput.type === 'password' ? 'text' : 'password';
    passwordConfirmInput.type = type;
    this.textContent = type === 'password' ? '👁️' : '🙈';
});

// パスワード強度チェック
passwordInput.addEventListener('input', function() {
    const password = this.value;
    let strength = 0;
    let message = '';
    let color = '';
    
    if (password.length >= 8) strength++;
    if (password.length >= 12) strength++;
    if (/[a-z]/.test(password)) strength++;
    if (/[A-Z]/.test(password)) strength++;
    if (/[0-9]/.test(password)) strength++;
    if (/[^a-zA-Z0-9]/.test(password)) strength++;
    
    if (password.length === 0) {
        passwordStrength.innerHTML = '';
        return;
    }
    
    if (strength <= 2) {
        message = '弱い';
        color = '#ff4444';
    } else if (strength <= 4) {
        message = '普通';
        color = '#ffaa00';
    } else {
        message = '強い';
        color = '#00cc44';
    }
    
    passwordStrength.innerHTML = `
        <div style="display: flex; align-items: center; gap: 10px; margin-top: 8px;">
            <div style="flex: 1; height: 4px; background: #e0e0e0; border-radius: 2px; overflow: hidden;">
                <div style="width: ${(strength / 6) * 100}%; height: 100%; background: ${color}; transition: all 0.3s;"></div>
            </div>
            <span style="color: ${color}; font-size: 0.9rem; font-weight: 600;">${message}</span>
        </div>
    `;
});

// パスワード一致チェック
passwordConfirmInput.addEventListener('input', function() {
    if (this.value === '') {
        passwordMatch.textContent = '';
        passwordMatch.style.color = '';
        return;
    }
    
    if (passwordInput.value === this.value) {
        passwordMatch.textContent = '✓ パスワードが一致しています';
        passwordMatch.style.color = '#00cc44';
    } else {
        passwordMatch.textContent = '✗ パスワードが一致しません';
        passwordMatch.style.color = '#ff4444';
    }
});

// 利用規約チェックでボタン有効化
agreeTermsCheckbox.addEventListener('change', function() {
    submitBtn.disabled = !this.checked;
});

// ユーザー名バリデーション（英数字とアンダースコアのみ）
usernameInput.addEventListener('input', function() {
    this.value = this.value.replace(/[^a-zA-Z0-9_]/g, '');
});

// フォーム送信
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // メッセージをリセット
    errorMessage.style.display = 'none';
    successMessage.style.display = 'none';
    
    // フォームデータ取得
    const username = usernameInput.value.trim();
    const email = emailInput.value.trim();
    const displayName = displayNameInput.value.trim();
    const password = passwordInput.value;
    const passwordConfirm = passwordConfirmInput.value;
    const agreeTerms = agreeTermsCheckbox.checked;
    
    // バリデーション
    if (!username || !email || !displayName || !password || !passwordConfirm) {
        showError('すべてのフィールドを入力してください');
        return;
    }
    
    if (username.length < 3) {
        showError('ユーザー名は3文字以上で入力してください');
        return;
    }
    
    if (!/^[a-zA-Z0-9_]+$/.test(username)) {
        showError('ユーザー名は英数字とアンダースコアのみ使用できます');
        return;
    }
    
    if (password.length < 8) {
        showError('パスワードは8文字以上で入力してください');
        return;
    }
    
    if (password !== passwordConfirm) {
        showError('パスワードが一致しません');
        return;
    }
    
    if (!agreeTerms) {
        showError('利用規約に同意してください');
        return;
    }
    
    // ボタンを無効化
    submitBtn.disabled = true;
    submitBtn.textContent = '登録中...';
    
    try {
        // JWT認証API呼び出し
        const response = await fetch('/api/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username,
                email,
                password,
                display_name: displayName  // 表示名も送信
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // トークンをlocalStorageに保存
            localStorage.setItem('access_token', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);
            localStorage.setItem('user', JSON.stringify({
                ...data.user,
                display_name: displayName
            }));
            
            // 成功メッセージ
            showSuccess(`🎉 登録成功！ようこそ ${displayName} さん！\n登録ボーナス: 10 SG を獲得しました！`);
            
            // リダイレクト
            setTimeout(() => {
                window.location.href = '/';
            }, 2000);
            
        } else {
            showError(data.error || '登録に失敗しました');
            submitBtn.disabled = false;
            submitBtn.textContent = '✨ アカウントを作成する';
        }
        
    } catch (error) {
        console.error('Register error:', error);
        showError('登録に失敗しました。もう一度お試しください。');
        submitBtn.disabled = false;
        submitBtn.textContent = '✨ アカウントを作成する';
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
    console.log('✅ Register page loaded');
    
    // 既にログイン済みの場合はリダイレクト
    const token = localStorage.getItem('access_token');
    if (token) {
        console.log('Already logged in, redirecting...');
        window.location.href = '/';
    }
});