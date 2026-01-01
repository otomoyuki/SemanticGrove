// 記憶の巨大樹 - JavaScript (Phase 1対応)

// 全投稿データを保持
let allPosts = [];

// 初期化
document.addEventListener('DOMContentLoaded', () => {
    loadSGBalance();
    loadPosts();
    setupTabs();
    setupForm();
});

// SGポイント残高を取得
async function loadSGBalance() {
    try {
        const response = await fetch('/api/sg/balance');
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('sgPoints').textContent = data.balance;
            
            if (data.bonus > 0) {
                showSuccessMessage(`ログインボーナス +${data.bonus} SG を獲得！`);
            }
        }
    } catch (error) {
        console.error('SGポイント取得エラー:', error);
    }
}

// 投稿一覧を取得
async function loadPosts() {
    try {
        const response = await fetch('/api/memory-tree/posts');
        const data = await response.json();
        
        if (data.success && data.posts.length > 0) {
            allPosts = data.posts;
            displayPosts(allPosts);
        } else {
            document.getElementById('postsGrid').innerHTML = `
                <div class="loading">
                    まだ作品が投稿されていません。<br>
                    最初の作品を投稿しませんか？
                </div>
            `;
        }
    } catch (error) {
        console.error('投稿読み込みエラー:', error);
        document.getElementById('postsGrid').innerHTML = `
            <div class="loading">読み込みに失敗しました</div>
        `;
    }
}

// 投稿を表示
function displayPosts(posts) {
    const grid = document.getElementById('postsGrid');
    
    if (posts.length === 0) {
        grid.innerHTML = `
            <div class="loading">
                該当する作品が見つかりません
            </div>
        `;
        return;
    }
    
    grid.innerHTML = posts.map(post => createPostCard(post)).join('');
}

// 投稿カードを生成
function createPostCard(post) {
    const categoryNames = {
        'novel': '📖 小説',
        'poem': '✍️ 詩',
        'haiku': '🍃 俳句・短歌',
        'tweet': '💭 つぶやき',
        'essay': '📰 エッセイ',
        'illustration': '🎨 イラスト',
        'car_design': '🚗 車デザイン',
        'architecture': '🏠 建築デザイン',
        'fashion': '👗 ファッション',
        'game_idea': '🎮 ゲームアイデア',
        'other': 'その他'
    };
    
    const postTypeNames = {
        'text': '📝 テキスト',
        'image': '🖼️ 画像',
        'both': '📝+🖼️'
    };
    
    const date = new Date(post.created_at);
    const dateStr = `${date.getFullYear()}/${date.getMonth()+1}/${date.getDate()}`;
    
    // プレビューを100文字に制限
    const preview = post.content && post.content.length > 100 
        ? post.content.substring(0, 100) + '...' 
        : (post.content || '');
    
    // 画像がある場合
    const imageHTML = post.image_path 
        ? `<img src="${post.image_path}" alt="${escapeHtml(post.title)}" class="post-image">` 
        : '';
    
    return `
        <div class="post-card" onclick="showPost(${post.id})">
            ${imageHTML}
            <div class="post-content">
                <span class="post-type-badge">${postTypeNames[post.post_type] || '📝'}</span>
                <span class="post-category">${categoryNames[post.category] || 'その他'}</span>
                <h3 class="post-title">${escapeHtml(post.title)}</h3>
                ${preview ? `<p class="post-preview">${escapeHtml(preview)}</p>` : ''}
                <div class="post-meta">
                    <span class="post-date">📅 ${dateStr}</span>
                    <span class="post-likes">❤️ ${post.likes}</span>
                </div>
            </div>
        </div>
    `;
}

// フィルター機能
function filterPosts() {
    const categoryFilter = document.getElementById('categoryFilter').value;
    const typeFilter = document.getElementById('typeFilter').value;
    
    let filteredPosts = allPosts;
    
    // カテゴリーでフィルター
    if (categoryFilter) {
        filteredPosts = filteredPosts.filter(post => post.category === categoryFilter);
    }
    
    // タイプでフィルター
    if (typeFilter) {
        filteredPosts = filteredPosts.filter(post => post.post_type === typeFilter);
    }
    
    displayPosts(filteredPosts);
}

// 投稿詳細を表示
async function showPost(postId) {
    try {
        const response = await fetch(`/api/memory-tree/posts/${postId}`);
        const data = await response.json();
        
        if (data.success) {
            const post = data.post;
            const categoryNames = {
                'novel': '📖 小説',
                'poem': '✍️ 詩',
                'haiku': '🍃 俳句・短歌',
                'tweet': '💭 つぶやき',
                'essay': '📰 エッセイ',
                'illustration': '🎨 イラスト',
                'car_design': '🚗 車デザイン',
                'architecture': '🏠 建築デザイン',
                'fashion': '👗 ファッション',
                'game_idea': '🎮 ゲームアイデア',
                'other': 'その他'
            };
            
            const date = new Date(post.created_at);
            const dateStr = `${date.getFullYear()}年${date.getMonth()+1}月${date.getDate()}日`;
            
            // 画像がある場合
            const imageHTML = post.image_path 
                ? `<img src="${post.image_path}" alt="${escapeHtml(post.title)}" class="modal-image">` 
                : '';
            
            document.getElementById('modalContent').innerHTML = `
                ${imageHTML}
                <div class="post-category">${categoryNames[post.category] || 'その他'}</div>
                <h2>${escapeHtml(post.title)}</h2>
                <div class="post-meta">
                    <span class="post-date">📅 ${dateStr}</span>
                    <span class="post-likes">❤️ ${post.likes}</span>
                </div>
                ${post.content ? `
                    <div style="margin-top: 30px; white-space: pre-wrap; line-height: 1.8; color: #a5d6a7;">
                        ${escapeHtml(post.content)}
                    </div>
                ` : ''}
            `;
            
            document.getElementById('postModal').classList.add('show');
        }
    } catch (error) {
        console.error('投稿詳細取得エラー:', error);
    }
}

// モーダルを閉じる
function closePostModal() {
    document.getElementById('postModal').classList.remove('show');
}

// タブ切り替え
function setupTabs() {
    const tabs = document.querySelectorAll('.tab');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tabContents.forEach(tc => tc.classList.remove('active'));
            
            tab.classList.add('active');
            
            const tabName = tab.dataset.tab;
            document.getElementById(`${tabName}-tab`).classList.add('active');
        });
    });
}

// フォームのセットアップ
function setupForm() {
    const form = document.getElementById('postForm');
    const content = document.getElementById('content');
    const charCount = document.getElementById('charCount');
    
    // 文字数カウント
    content.addEventListener('input', () => {
        const count = content.value.length;
        charCount.textContent = count;
        
        if (count > 1900) {
            charCount.style.color = '#ef5350';
        } else if (count > 1700) {
            charCount.style.color = '#ffd54f';
        } else {
            charCount.style.color = '#a5d6a7';
        }
    });
    
    // フォーム送信
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const submitBtn = document.getElementById('submitBtn');
        submitBtn.disabled = true;
        submitBtn.textContent = '投稿中...';
        
        const formData = new FormData(form);
        
        try {
            const response = await fetch('/api/memory-tree/post', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (data.success) {
                showSuccessMessage(`✅ 作品を投稿しました！+${data.sg_bonus} SG を獲得！`);
                
                form.reset();
                charCount.textContent = '0';
                removeImage();
                
                loadSGBalance();
                loadPosts();
                
                document.querySelector('.tab[data-tab="posts"]').click();
            } else {
                alert('投稿に失敗しました: ' + data.error);
            }
        } catch (error) {
            console.error('投稿エラー:', error);
            alert('投稿に失敗しました');
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = '🌳 作品を投稿する (+1 SG)';
        }
    });
}

// 投稿タイプに応じて表示を切り替え
function toggleContentFields() {
    const postType = document.getElementById('postType').value;
    const textGroup = document.getElementById('textGroup');
    const imageGroup = document.getElementById('imageGroup');
    const descriptionGroup = document.getElementById('descriptionGroup');
    const contentField = document.getElementById('content');
    
    if (postType === 'text') {
        textGroup.style.display = 'block';
        imageGroup.style.display = 'none';
        descriptionGroup.style.display = 'none';
        contentField.required = true;
    } else if (postType === 'image') {
        textGroup.style.display = 'none';
        imageGroup.style.display = 'block';
        descriptionGroup.style.display = 'block';
        contentField.required = false;
    } else { // both
        textGroup.style.display = 'block';
        imageGroup.style.display = 'block';
        descriptionGroup.style.display = 'none';
        contentField.required = true;
    }
}

// カテゴリーに応じて投稿タイプのオプションを調整
function updatePostTypeOptions() {
    const category = document.getElementById('category').value;
    const postType = document.getElementById('postType');
    
    const textCategories = ['novel', 'poem', 'haiku', 'tweet', 'essay'];
    const imageCategories = ['illustration', 'car_design', 'architecture', 'fashion'];
    
    // デフォルト値を設定
    if (textCategories.includes(category)) {
        postType.value = 'text';
    } else if (imageCategories.includes(category)) {
        postType.value = 'image';
    }
    
    toggleContentFields();
}

// 画像プレビュー
function previewImage(event) {
    const file = event.target.files[0];
    
    if (!file) return;
    
    // ファイルサイズチェック (5MB)
    if (file.size > 5 * 1024 * 1024) {
        alert('画像サイズは5MB以内にしてください');
        event.target.value = '';
        return;
    }
    
    // ファイルタイプチェック
    if (!file.type.match('image/(png|jpeg|jpg)')) {
        alert('PNG, JPG形式のみ対応しています。\n\nCADデータをお持ちの方は、レンダリング画像やスクリーンショットに変換してから投稿してください。');
        event.target.value = '';
        return;
    }
    
    const reader = new FileReader();
    
    reader.onload = function(e) {
        document.getElementById('uploadPlaceholder').style.display = 'none';
        document.getElementById('imagePreview').style.display = 'block';
        document.getElementById('previewImg').src = e.target.result;
    };
    
    reader.readAsDataURL(file);
}

// 画像削除
function removeImage() {
    document.getElementById('image').value = '';
    document.getElementById('uploadPlaceholder').style.display = 'block';
    document.getElementById('imagePreview').style.display = 'none';
    document.getElementById('previewImg').src = '';
}

// 成功メッセージを表示
function showSuccessMessage(message) {
    const msgEl = document.getElementById('successMessage');
    msgEl.textContent = message;
    msgEl.classList.add('show');
    
    setTimeout(() => {
        msgEl.classList.remove('show');
    }, 3000);
}

// 公式ストーリーを表示
function showOfficialStory(storyId) {
    const stories = {
        'beginning': {
            title: '始まりの記憶',
            content: `
遥か昔、言葉が生まれる前の時代。

人々は意味を探し求めていた。
音があり、身振りがあり、感情があった。
しかし、それらをつなぐ「言葉」という概念は、まだ存在していなかった。

ある日、平原の中央に、一本の小さな芽が姿を現した。
それは見る者すべてに、何か大切なことを思い出させる不思議な力を持っていた。

人々はその芽の周りに集まり、自分たちが感じていることを
音や身振りで表現し始めた。

そして、その表現が他の人に伝わったとき、
小さな芽は少しずつ成長していった。

何千年もの時を経て、その芽は巨大な樹へと成長した。
人々の記憶、想い、言葉、意味。
すべてがこの樹に刻まれ、守られている。

これが、「記憶の巨大樹」の始まりである。
            `
        },
        'seeker': {
            title: '意味の探求者',
            content: `
SemanticFieldには、かつて一人の探求者がいた。

彼の名はアルカナ。
言葉の意味を追い求め、世界中を旅していた。

アルカナは問い続けた。
「なぜ、同じ言葉が異なる意味を持つのか？」
「なぜ、言葉は時代とともに変化するのか？」
「言葉の本当の意味とは、一体何なのか？」

ある日、彼はこの平原にたどり着いた。
そこで彼が見たのは、輝く巨大な樹だった。

樹は彼に語りかけた。
「意味とは、固定されたものではない。
 意味とは、人々が紡ぐ物語そのものだ。」

アルカナは理解した。
言葉の意味は、辞書の中にあるのではなく、
人々が使い、感じ、共有する瞬間にこそ存在するのだと。

彼は樹の下で瞑想し、自らの探求の旅を記憶として刻んだ。

そして、次の探求者のために、この地を「SemanticField」と名付けた。
意味を探求するすべての者のための、聖域として。
            `
        },
        'guardian': {
            title: '樹の守護者',
            content: `
記憶の巨大樹を守る者たちがいる。

彼らは「守護者」と呼ばれ、世代を超えて樹を守り続けている。

守護者の役割は、樹に刻まれた記憶を保護し、
次の世代へと継承することだ。

しかし、彼らの真の使命は、それだけではない。

守護者は、訪れる者すべてに問いかける。
「あなたはなぜ、ここに来たのか？」
「あなたは何を探しているのか？」
「あなたは何を残したいのか？」

そして、その答えを聞き、導く。

ある守護者は語った。
「私たちは、記憶を守っているのではない。
 私たちは、意味を紡ぐ人々を守っているのだ。」

記憶の巨大樹は、ただの樹ではない。
それは、人々の想いが集まり、新しい意味が生まれる場所。

守護者たちは、その場所を守り続ける。
永遠に。
            `
        }
    };
    
    const story = stories[storyId];
    if (story) {
        document.getElementById('storyContent').innerHTML = `
            <h2>${story.title}</h2>
            <div style="white-space: pre-wrap; line-height: 1.8; color: #a5d6a7;">
                ${story.content.trim()}
            </div>
        `;
        document.getElementById('storyModal').classList.add('show');
    }
}

// ストーリーモーダルを閉じる
function closeStoryModal() {
    document.getElementById('storyModal').classList.remove('show');
}

// HTMLエスケープ
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// モーダルの外側をクリックしたら閉じる
window.addEventListener('click', (e) => {
    const postModal = document.getElementById('postModal');
    const storyModal = document.getElementById('storyModal');
    
    if (e.target === postModal) {
        closePostModal();
    }
    if (e.target === storyModal) {
        closeStoryModal();
    }
});