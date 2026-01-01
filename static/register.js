// register.js - アカウント作成画面の機能

document.addEventListener('DOMContentLoaded', () => {
    // 要素取得
    const form = document.getElementById('registerForm');
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const displayName = document.getElementById('displayName');
    const password = document.getElementById('password');
    const passwordConfirm = document.getElementById('passwordConfirm');
    const agreeTerms = document.getElementById('agreeTerms');
    const submitBtn = document.getElementById('submitBtn');
    const errorMessage = document.getElementById('errorMessage');
    const passwordStrength = document.getElementById('passwordStrength');
    const passwordMatch = document.getElementById('passwordMatch');
    const togglePassword = document.getElementById('togglePassword');
    const togglePasswordConfirm = document.getElementById('togglePasswordConfirm');

    // パスワード表示切り替え
    togglePassword.addEventListener('click', () => {
        const type = password.type === 'password' ? 'text' : 'password';
        password.type = type;
        togglePassword.textContent = type === 'password' ? '👁️' : '🙈';
    });

    togglePasswordConfirm.addEventListener('click', () => {
        const type = passwordConfirm.type === 'password' ? 'text' : 'password';
        passwordConfirm.type = type;
        togglePasswordConfirm.textContent = type === 'password' ? '👁️' : '🙈';
    });

    // パスワード強度チェック
    password.addEventListener('input', () => {
        const value = password.value;
        let strength = 0;

        if (value.length >= 8) strength++;
        if (value.length >= 12) strength++;
        if (/[a-z]/.test(value) && /[A-Z]/.test(value)) strength++;
        if (/\d/.test(value)) strength++;
        if (/[^a-zA-Z0-9]/.test(value)) strength++;

        passwordStrength.className = 'password-strength';
        if (strength <= 2) {
            passwordStrength.classList.add('weak');
        } else if (strength <= 4) {
            passwordStrength.classList.add('medium');
        } else {
            passwordStrength.classList.add('strong');
        }

        // パスワード一致チェック
        checkPasswordMatch();
    });

    // パスワード確認チェック
    passwordConfirm.addEventListener('input', checkPasswordMatch);

    function checkPasswordMatch() {
        if (passwordConfirm.value === '') {
            passwordMatch.textContent = '';
            passwordMatch.className = '';
            return;
        }

        if (password.value === passwordConfirm.value) {
            passwordMatch.textContent = '✓ パスワードが一致しています';
            passwordMatch.className = 'help-text match';
        } else {
            passwordMatch.textContent = '✗ パスワードが一致していません';
            passwordMatch.className = 'help-text no-match';
        }
    }

    // ユーザー名バリデーション（英数字とアンダースコアのみ）
    username.addEventListener('input', () => {
        const value = username.value;
        const valid = /^[a-zA-Z0-9_]*$/.test(value);
        
        if (!valid && value !== '') {
            username.setCustomValidity('英数字とアンダースコアのみ使用できます');
        } else {
            username.setCustomValidity('');
        }
    });

    // 送信ボタンの有効化チェック
    function checkFormValidity() {
        const isValid = 
            username.value.length >= 3 &&
            email.validity.valid &&
            displayName.value.trim() !== '' &&
            password.value.length >= 8 &&
            password.value === passwordConfirm.value &&
            agreeTerms.checked;

        submitBtn.disabled = !isValid;
    }

    // 入力フィールドの変更を監視
    [username, email, displayName, password, passwordConfirm, agreeTerms].forEach(element => {
        element.addEventListener('input', checkFormValidity);
        element.addEventListener('change', checkFormValidity);
    });

    // 利用規約同意チェックボックスの強調
    agreeTerms.addEventListener('change', () => {
        const label = agreeTerms.closest('.checkbox-label');
        if (agreeTerms.checked) {
            label.style.animation = 'none';
        }
    });

    // フォーム送信
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // 最終チェック
        if (!agreeTerms.checked) {
            showError('利用規約に同意してください');
            return;
        }

        if (password.value !== passwordConfirm.value) {
            showError('パスワードが一致していません');
            return;
        }

        // ローディング状態
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;

        try {
            // APIリクエスト
            const response = await fetch('/api/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: username.value,
                    email: email.value,
                    displayName: displayName.value,
                    password: password.value,
                    agreedToTerms: true,
                    agreedAt: new Date().toISOString()
                }),
            });

            const data = await response.json();

            if (response.ok && data.success) {
                // 成功 - ログインページまたはトップページへ
                sessionStorage.setItem('registrationSuccess', 'true');
                window.location.href = data.redirect || '/login?registered=true';
            } else {
                showError(data.error || '登録に失敗しました');
            }
        } catch (error) {
            console.error('Registration error:', error);
            showError('ネットワークエラーが発生しました');
        } finally {
            submitBtn.classList.remove('loading');
            submitBtn.disabled = false;
            checkFormValidity();
        }
    });

    // エラー表示
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        
        // エラーメッセージにスクロール
        errorMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });

        // 5秒後に自動非表示
        setTimeout(() => {
            errorMessage.style.display = 'none';
        }, 5000);
    }

    // URLパラメータチェック（利用規約から戻ってきた場合）
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('agreed') === 'true') {
        agreeTerms.checked = true;
        checkFormValidity();
        
        // スムーズにフォームの先頭にスクロール
        setTimeout(() => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }, 100);
    }

    // 初回チェック
    checkFormValidity();
});