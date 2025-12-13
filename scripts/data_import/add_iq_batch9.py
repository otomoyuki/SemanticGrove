import sqlite3
import json
import os

DB_NAME = "SemanticGrove.db"
IMAGE_DIR = "static/images"

# ==================== SVG生成関数（第9弾） ====================

def generate_batch9_svgs():
    """第9弾のSVGパターンを生成（51-100）"""
    svgs = []
    
    # パターン51-60：時計の角度問題
    for i in range(51, 61):
        hour = (i - 50) % 12
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">時計パターン{i}：次の時刻は？</text>
  <circle cx="200" cy="180" r="60" fill="white" stroke="#333" stroke-width="3"/>
  <line x1="200" y1="180" x2="200" y2="140" stroke="#333" stroke-width="3"/>
  <line x1="200" y1="180" x2="230" y2="180" stroke="#e11d48" stroke-width="2"/>
  <text x="450" y="190" font-size="40" text-anchor="middle" fill="#666">?</text>
  <text x="300" y="320" font-size="14" text-anchor="middle" fill="#666">2時間後は？</text>
</svg>'''
        svgs.append(svg)
    
    # パターン61-70：ベン図問題
    for i in range(61, 71):
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">ベン図{i}：重なりの人数は？</text>
  <circle cx="220" cy="180" r="70" fill="#3b82f6" opacity="0.3" stroke="#333" stroke-width="2"/>
  <circle cx="320" cy="180" r="70" fill="#ef4444" opacity="0.3" stroke="#333" stroke-width="2"/>
  <text x="180" y="185" font-size="20" text-anchor="middle" fill="#333">{i-50}</text>
  <text x="270" y="185" font-size="20" text-anchor="middle" fill="#333">?</text>
  <text x="360" y="185" font-size="20" text-anchor="middle" fill="#333">{i-55}</text>
  <text x="150" y="290" font-size="14" fill="#333">数学:{i-40}人</text>
  <text x="350" y="290" font-size="14" fill="#333">英語:{i-45}人</text>
</svg>'''
        svgs.append(svg)
    
    # パターン71-80：座標平面上の点
    for i in range(71, 81):
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">座標問題{i}：次の点は？</text>
  <line x1="100" y1="300" x2="500" y2="300" stroke="#333" stroke-width="2"/>
  <line x1="100" y1="100" x2="100" y2="300" stroke="#333" stroke-width="2"/>
  <circle cx="150" cy="250" r="5" fill="#10b981"/>
  <circle cx="200" cy="200" r="5" fill="#10b981"/>
  <circle cx="250" cy="150" r="5" fill="#10b981"/>
  <text x="350" y="180" font-size="40" text-anchor="middle" fill="#e11d48">?</text>
  <text x="300" y="350" font-size="14" text-anchor="middle" fill="#666">y = -x + c のパターン</text>
</svg>'''
        svgs.append(svg)
    
    # パターン81-90：天秤問題
    for i in range(81, 91):
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">天秤{i}：釣り合うには？</text>
  <line x1="150" y1="150" x2="450" y2="150" stroke="#333" stroke-width="4"/>
  <circle cx="300" cy="150" r="8" fill="#333"/>
  <rect x="170" y="160" width="40" height="40" fill="#f59e0b" stroke="#333" stroke-width="2"/>
  <rect x="190" y="160" width="40" height="40" fill="#f59e0b" stroke="#333" stroke-width="2"/>
  <text x="420" y="190" font-size="36" text-anchor="middle" fill="#e11d48">?</text>
  <text x="300" y="280" font-size="14" text-anchor="middle" fill="#666">左:{i-80}kg</text>
</svg>'''
        svgs.append(svg)
    
    # パターン91-100：論理回路
    for i in range(91, 101):
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">論理回路{i}：出力は？</text>
  <rect x="150" y="120" width="100" height="60" fill="#ddd" stroke="#333" stroke-width="2"/>
  <text x="200" y="155" font-size="16" text-anchor="middle" fill="#333">AND</text>
  <line x1="100" y1="135" x2="150" y2="135" stroke="#333" stroke-width="2"/>
  <line x1="100" y1="165" x2="150" y2="165" stroke="#333" stroke-width="2"/>
  <line x1="250" y1="150" x2="300" y2="150" stroke="#333" stroke-width="2"/>
  <text x="80" y="140" font-size="14" fill="#333">A=1</text>
  <text x="80" y="170" font-size="14" fill="#333">B={(i-90)%2}</text>
  <text x="320" y="160" font-size="30" text-anchor="middle" fill="#e11d48">?</text>
</svg>'''
        svgs.append(svg)
    
    return svgs

def create_batch9_svg_files():
    """第9弾のSVGファイルを生成"""
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    
    print("=" * 60)
    print("SVGファイル生成中（第9弾：51-100）...")
    print("=" * 60)
    
    svgs = generate_batch9_svgs()
    
    for i, svg_content in enumerate(svgs, 51):
        filename = f"iq_batch9_{i:03d}.svg"
        filepath = os.path.join(IMAGE_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        if i <= 55 or i >= 96:  # 最初と最後だけ表示
            print(f"✓ {filename}")
        elif i == 56:
            print(f"  ... (56-95を生成中)")
    
    print(f"\n✓ 50個のSVGファイルを作成しました（51-100）")

def add_iq_batch9():
    """IQ問題追加（第9弾・50問）"""
    
    # SVGファイルを生成
    create_batch9_svg_files()
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("\n" + "=" * 60)
    print("IQ問題追加スクリプト（第9弾）")
    print("=" * 60)
    
    questions = []
    
    # 時計問題（51-60）
    print("[1/5] 時計パターン問題を生成中...")
    for i in range(51, 61):
        hour = (i - 50) % 12
        questions.append((
            f"時計が{hour}時を指している。2時間後は？",
            f"images/iq_batch9_{i:03d}.svg",
            [
                {"id":"A","text":f"{(hour+1)%12}時"},
                {"id":"B","text":f"{(hour+2)%12}時"},
                {"id":"C","text":f"{(hour+3)%12}時"},
                {"id":"D","text":f"{(hour+4)%12}時"}
            ],
            [1],
            "時計算",
            "3",
            10,
            "2時間後を計算",
            "時刻計算"
        ))
    print(f"  ✓ 時計問題: 10問")
    
    # ベン図問題（61-70）
    print("[2/5] ベン図問題を生成中...")
    for i in range(61, 71):
        total_math = i - 40
        total_english = i - 45
        both = (i - 60) + 3
        questions.append((
            f"数学{total_math}人、英語{total_english}人、両方{both}人。数学のみは？",
            f"images/iq_batch9_{i:03d}.svg",
            [
                {"id":"A","text":f"{total_math-both}人"},
                {"id":"B","text":f"{total_math-both+1}人"},
                {"id":"C","text":f"{total_math-both-1}人"},
                {"id":"D","text":f"{total_math}人"}
            ],
            [0],
            "集合",
            "3",
            12,
            "ベン図の計算",
            "集合演算"
        ))
    print(f"  ✓ ベン図問題: 10問")
    
    # 座標問題（71-80）
    print("[3/5] 座標問題を生成中...")
    for i in range(71, 81):
        questions.append((
            f"座標パターン{i}：規則的に並ぶ点の次は？",
            f"images/iq_batch9_{i:03d}.svg",
            [
                {"id":"A","text":"(300, 100)"},
                {"id":"B","text":"(350, 150)"},
                {"id":"C","text":"(300, 150)"},
                {"id":"D","text":"(350, 100)"}
            ],
            [0],
            "座標",
            "4",
            15,
            "座標の規則性",
            "数列パターン"
        ))
    print(f"  ✓ 座標問題: 10問")
    
    # 天秤問題（81-90）
    print("[4/5] 天秤問題を生成中...")
    for i in range(81, 91):
        left_weight = i - 80
        questions.append((
            f"天秤の左に{left_weight}kg。釣り合うには右に？",
            f"images/iq_batch9_{i:03d}.svg",
            [
                {"id":"A","text":f"{left_weight}kg"},
                {"id":"B","text":f"{left_weight+1}kg"},
                {"id":"C","text":f"{left_weight-1}kg"},
                {"id":"D","text":f"{left_weight*2}kg"}
            ],
            [0],
            "天秤算",
            "3",
            10,
            "重さの釣り合い",
            "重量計算"
        ))
    print(f"  ✓ 天秤問題: 10問")
    
    # 論理回路問題（91-100）
    print("[5/5] 論理回路問題を生成中...")
    for i in range(91, 101):
        b_value = (i - 90) % 2
        output = 1 if b_value == 1 else 0
        questions.append((
            f"論理AND回路：A=1, B={b_value}のとき出力は？",
            f"images/iq_batch9_{i:03d}.svg",
            [
                {"id":"A","text":"0"},
                {"id":"B","text":"1"},
                {"id":"C","text":"不定"},
                {"id":"D","text":"エラー"}
            ],
            [output],
            "論理回路",
            "4",
            15,
            "AND演算の結果",
            "論理演算"
        ))
    print(f"  ✓ 論理回路問題: 10問")
    
    # データベースに挿入
    print("\nデータベースに保存中...")
    for q in questions:
        question_json = {
            "question": q[0],
            "image": q[1],
            "options": q[2],
            "answer": q[3]
        }
        
        cursor.execute("""
            INSERT INTO questions 
            (language, question_json, category, difficulty, score, meaning, usage)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ("IQ", json.dumps(question_json, ensure_ascii=False), 
              q[4], q[5], q[6], q[7], q[8]))
    
    conn.commit()
    
    # 統計表示
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'IQ'")
    iq_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("=" * 60)
    print("✓ IQ問題追加完了（第9弾）！")
    print("=" * 60)
    print(f"IQ問題数: {iq_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"目標500問まで残り: {max(0, 500 - iq_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_iq_batch9()