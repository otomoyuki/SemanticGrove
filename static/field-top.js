// SemanticField トップページ - JavaScript

// 現在のビューモード（'2d' or '3d'）
let currentView = '2d';

// ドラッグ/スワイプ用の変数
let startX = 0;
let isDragging = false;
const SWIPE_THRESHOLD = 100; // スワイプと判定する最小距離（px）

// 初期化
document.addEventListener('DOMContentLoaded', () => {
    // LocalStorageから前回のビュー設定を読み込み
    const savedView = localStorage.getItem('semanticfield_view');
    if (savedView === '3d') {
        switchTo3D();
    } else {
        switchTo2D();
    }
    
    // ドラッグイベントの設定
    setupDragEvents();
    
    // スワイプヒントを3秒後に非表示
    setTimeout(() => {
        const hint = document.getElementById('swipeHint');
        if (hint) {
            hint.style.opacity = '0';
            setTimeout(() => hint.style.display = 'none', 500);
        }
    }, 3000);
});

// 2Dマップに切り替え
function switchTo2D() {
    currentView = '2d';
    
    // ビューの切り替え
    document.getElementById('view2d').classList.add('active');
    document.getElementById('view3d').classList.remove('active');
    
    // ボタンの状態更新
    document.getElementById('btn2d').classList.add('active');
    document.getElementById('btn3d').classList.remove('active');
    
    // ビュー名更新
    document.getElementById('viewName').textContent = '2Dマップ';
    
    // LocalStorageに保存
    localStorage.setItem('semanticfield_view', '2d');
    
    console.log('🗺️ 2Dマップビューに切り替え');
}

// 3D鳥瞰図に切り替え
function switchTo3D() {
    currentView = '3d';
    
    // ビューの切り替え
    document.getElementById('view2d').classList.remove('active');
    document.getElementById('view3d').classList.add('active');
    
    // ボタンの状態更新
    document.getElementById('btn2d').classList.remove('active');
    document.getElementById('btn3d').classList.add('active');
    
    // ビュー名更新
    document.getElementById('viewName').textContent = '3D鳥瞰図';
    
    // LocalStorageに保存
    localStorage.setItem('semanticfield_view', '3d');
    
    console.log('🎬 3D鳥瞰図ビューに切り替え');
}

// ビューのトグル
function toggleView() {
    if (currentView === '2d') {
        switchTo3D();
    } else {
        switchTo2D();
    }
}

// ドラッグ/スワイプイベントの設定
function setupDragEvents() {
    const container = document.getElementById('fieldContainer');
    
    // マウスイベント（PC用）
    container.addEventListener('mousedown', handleDragStart);
    container.addEventListener('mousemove', handleDragMove);
    container.addEventListener('mouseup', handleDragEnd);
    container.addEventListener('mouseleave', handleDragEnd);
    
    // タッチイベント（スマホ/タブレット用）
    container.addEventListener('touchstart', handleTouchStart);
    container.addEventListener('touchmove', handleTouchMove);
    container.addEventListener('touchend', handleTouchEnd);
}

// ドラッグ開始（マウス）
function handleDragStart(e) {
    // リンクのクリックを妨げないように、カード外でのみドラッグ可能
    if (e.target.closest('.area-card')) {
        return;
    }
    
    isDragging = true;
    startX = e.clientX;
    console.log('ドラッグ開始:', startX);
}

// ドラッグ中（マウス）
function handleDragMove(e) {
    if (!isDragging) return;
    
    const currentX = e.clientX;
    const diffX = currentX - startX;
    
    // 視覚的フィードバック（オプション）
    if (Math.abs(diffX) > 30) {
        document.body.style.cursor = diffX > 0 ? 'e-resize' : 'w-resize';
    }
}

// ドラッグ終了（マウス）
function handleDragEnd(e) {
    if (!isDragging) return;
    
    const endX = e.clientX;
    const diffX = endX - startX;
    
    console.log('ドラッグ終了:', endX, 'diff:', diffX);
    
    // スワイプ判定
    if (Math.abs(diffX) > SWIPE_THRESHOLD) {
        if (diffX > 0) {
            // 右スワイプ → 2Dに
            console.log('右スワイプ検出 → 2D');
            switchTo2D();
        } else {
            // 左スワイプ → 3Dに
            console.log('左スワイプ検出 → 3D');
            switchTo3D();
        }
    }
    
    isDragging = false;
    document.body.style.cursor = '';
}

// タッチ開始（スマホ）
function handleTouchStart(e) {
    if (e.target.closest('.area-card')) {
        return;
    }
    
    isDragging = true;
    startX = e.touches[0].clientX;
    console.log('タッチ開始:', startX);
}

// タッチ移動（スマホ）
function handleTouchMove(e) {
    if (!isDragging) return;
    
    // スクロールを防止
    // e.preventDefault(); // 注意: カードのクリックを妨げる可能性あり
}

// タッチ終了（スマホ）
function handleTouchEnd(e) {
    if (!isDragging) return;
    
    const endX = e.changedTouches[0].clientX;
    const diffX = endX - startX;
    
    console.log('タッチ終了:', endX, 'diff:', diffX);
    
    // スワイプ判定
    if (Math.abs(diffX) > SWIPE_THRESHOLD) {
        if (diffX > 0) {
            // 右スワイプ → 2Dに
            console.log('右スワイプ検出 → 2D');
            switchTo2D();
        } else {
            // 左スワイプ → 3Dに
            console.log('左スワイプ検出 → 3D');
            switchTo3D();
        }
    }
    
    isDragging = false;
}

// キーボードショートカット（オプション）
document.addEventListener('keydown', (e) => {
    // 左矢印キー → 2D
    if (e.key === 'ArrowLeft') {
        switchTo2D();
    }
    // 右矢印キー → 3D
    else if (e.key === 'ArrowRight') {
        switchTo3D();
    }
    // スペースキー → トグル
    else if (e.key === ' ') {
        e.preventDefault();
        toggleView();
    }
});

// デバッグ用：現在のビューを表示
console.log('SemanticField トップページ読み込み完了');
console.log('初期ビュー:', currentView);