// terms.js - 利用規約ページの機能

document.addEventListener('DOMContentLoaded', () => {
    // 要素取得
    const toggleBtn = document.getElementById('toggleVersion');
    const toggleIcon = document.getElementById('toggleIcon');
    const toggleText = document.getElementById('toggleText');
    const version3 = document.getElementById('version3');
    const version1 = document.getElementById('version1');
    const agreeBtn = document.getElementById('agreeBtn');
    const declineBtn = document.getElementById('declineBtn');
    
    // 現在のバージョン（デフォルト: 3 = ビジネスライク）
    let currentVersion = 3;
    
    // バージョン切り替え
    toggleBtn.addEventListener('click', () => {
        if (currentVersion === 3) {
            // バージョン3 → バージョン1
            version3.classList.remove('active');
            version1.classList.add('active');
            toggleIcon.textContent = '⚖️';
            toggleText.textContent = '正式な規約を読む';
            currentVersion = 1;
        } else {
            // バージョン1 → バージョン3
            version1.classList.remove('active');
            version3.classList.add('active');
            toggleIcon.textContent = '📖';
            toggleText.textContent = '分かりやすく読む';
            currentVersion = 3;
        }
        
        // トップにスクロール
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // URLパラメータをチェック（アカウント作成画面から来た場合）
    const urlParams = new URLSearchParams(window.location.search);
    const fromRegister = urlParams.get('from') === 'register';
    
    if (fromRegister) {
        // 同意ボタンを表示
        document.getElementById('termsActions').style.display = 'flex';
    }
    
    // 同意ボタン
    if (agreeBtn) {
        agreeBtn.addEventListener('click', () => {
            // セッションストレージに同意フラグを保存
            sessionStorage.setItem('termsAgreed', 'true');
            
            // アカウント作成画面に戻る
            window.location.href = '/register?agreed=true';
        });
    }
    
    // 戻るボタン
    if (declineBtn) {
        declineBtn.addEventListener('click', () => {
            // アカウント作成画面に戻る
            window.location.href = '/register';
        });
    }
    
    // スムーズスクロール（アンカーリンク用）
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // 読了チェック（下までスクロールしたか）
    let hasScrolledToBottom = false;
    
    window.addEventListener('scroll', () => {
        const scrollPosition = window.scrollY + window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;
        
        // 90%以上スクロールしたら読了とみなす
        if (scrollPosition >= documentHeight * 0.9 && !hasScrolledToBottom) {
            hasScrolledToBottom = true;
            console.log('利用規約を最後まで読みました');
            
            // 同意ボタンを強調（もしあれば）
            if (agreeBtn && fromRegister) {
                agreeBtn.style.animation = 'pulse 1s infinite';
            }
        }
    });
});

// パルスアニメーション（CSS追加）
const style = document.createElement('style');
style.textContent = `
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
`;
document.head.appendChild(style);