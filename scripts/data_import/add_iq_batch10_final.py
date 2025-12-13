import sqlite3
import json
import os

DB_NAME = "SemanticGrove.db"
IMAGE_DIR = "static/images"

# ==================== SVG生成関数（第10弾・最終） ====================

def generate_batch10_svgs():
    """第10弾のSVGパターンを生成（101-149）"""
    svgs = []
    
    # パターン101-110：確率問題（サイコロ）
    for i in range(101, 111):
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">確率問題{i}：サイコロで{(i-100)%6+1}が出る確率は？</text>
  <rect x="220" y="120" width="80" height="80" fill="white" stroke="#333" stroke-width="3" rx="5"/>
  <circle cx="260" cy="140" r="6" fill="#333"/>
  <circle cx="260" cy="160" r="6" fill="#333"/>
  <circle cx="260" cy="180" r="6" fill="#333"/>
  <circle cx="280" cy="140" r="6" fill="#333"/>
  <circle cx="280" cy="160" r="6" fill="#333"/>
  <circle cx="280" cy="180" r="6" fill="#333"/>
  <text x="300" y="280" font-size="16" text-anchor="middle" fill="#666">1個のサイコロ</text>
</svg>'''
        svgs.append(svg)
    
    # パターン111-120：順列・組み合わせ
    for i in range(111, 121):
        n = (i - 110) + 2
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">組み合わせ{i}：{n}個から2個選ぶ方法は？</text>
  <circle cx="200" cy="140" r="30" fill="#3b82f6" stroke="#333" stroke-width="2"/>
  <circle cx="260" cy="140" r="30" fill="#10b981" stroke="#333" stroke-width="2"/>
  <circle cx="320" cy="140" r="30" fill="#f59e0b" stroke="#333" stroke-width="2"/>
  <circle cx="380" cy="140" r="30" fill="#ec4899" stroke="#333" stroke-width="2"/>
  <text x="300" y="220" font-size="20" text-anchor="middle" fill="#333">↓ 2個選ぶ ↓</text>
  <text x="300" y="280" font-size="16" text-anchor="middle" fill="#666">組み合わせの数は？</text>
</svg>'''
        svgs.append(svg)
    
    # パターン121-130：推移律問題
    for i in range(121, 131):
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">推移律{i}：A&gt;B、B&gt;C ならば？</text>
  <circle cx="150" cy="140" r="40" fill="#ef4444" stroke="#333" stroke-width="2"/>
  <text x="150" y="150" font-size="24" font-weight="bold" text-anchor="middle" fill="white">A</text>
  <line x1="190" y1="140" x2="240" y2="140" stroke="#333" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="215" y="130" font-size="16" fill="#333">&gt;</text>
  <circle cx="280" cy="140" r="40" fill="#3b82f6" stroke="#333" stroke-width="2"/>
  <text x="280" y="150" font-size="24" font-weight="bold" text-anchor="middle" fill="white">B</text>
  <line x1="320" y1="140" x2="370" y2="140" stroke="#333" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="345" y="130" font-size="16" fill="#333">&gt;</text>
  <circle cx="410" cy="140" r="40" fill="#10b981" stroke="#333" stroke-width="2"/>
  <text x="410" y="150" font-size="24" font-weight="bold" text-anchor="middle" fill="white">C</text>
  <text x="300" y="250" font-size="20" text-anchor="middle" fill="#666">A と C の関係は？</text>
</svg>'''
        svgs.append(svg)
    
    # パターン131-140：面積問題
    for i in range(131, 141):
        side = (i - 130) + 3
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">面積問題{i}：一辺{side}cmの正方形の面積は？</text>
  <rect x="220" y="100" width="{side*20}" height="{side*20}" fill="#a78bfa" opacity="0.5" stroke="#333" stroke-width="2"/>
  <text x="{220+side*10}" y="{100+side*10+5}" font-size="20" font-weight="bold" text-anchor="middle" fill="#333">{side}cm</text>
  <text x="300" y="280" font-size="16" text-anchor="middle" fill="#666">面積 = ？ cm²</text>
</svg>'''
        svgs.append(svg)
    
    # パターン141-149：最終問題（総合）
    for i in range(141, 150):
        problem_num = i - 140
        svg = f'''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="20" font-weight="bold" text-anchor="middle" fill="#333">🎉 最終問題 {problem_num}/9 🎉</text>
  <rect x="150" y="80" width="300" height="220" fill="#f0f9ff" stroke="#3b82f6" stroke-width="3" rx="10"/>
  <text x="300" y="120" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">総合問題 #{i}</text>
  <circle cx="200" cy="170" r="25" fill="#ef4444" stroke="#333" stroke-width="2"/>
  <rect x="265" y="145" width="50" height="50" fill="#10b981" stroke="#333" stroke-width="2"/>
  <polygon points="380,145 405,195 355,195" fill="#f59e0b" stroke="#333" stroke-width="2"/>
  <text x="300" y="250" font-size="16" text-anchor="middle" fill="#666">パターンを見つけよ</text>
  <text x="300" y="350" font-size="14" font-style="italic" text-anchor="middle" fill="#999">あと{10-problem_num}問で500問達成！</text>
</svg>'''
        svgs.append(svg)
    
    return svgs

def create_batch10_svg_files():
    """第10弾のSVGファイルを生成"""
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    
    print("=" * 60)
    print("SVGファイル生成中（第10弾：101-149）...")
    print("=" * 60)
    
    svgs = generate_batch10_svgs()
    
    for i, svg_content in enumerate(svgs, 101):
        filename = f"iq_batch10_{i:03d}.svg"
        filepath = os.path.join(IMAGE_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        if i <= 105 or i >= 145:  # 最初と最後だけ表示
            print(f"✓ {filename}")
        elif i == 106:
            print(f"  ... (106-144を生成中)")
    
    print(f"\n✓ 49個のSVGファイルを作成しました（101-149）")

def add_iq_batch10_final():
    """IQ問題追加（第10弾・最終49問）"""
    
    # SVGファイルを生成
    create_batch10_svg_files()
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("\n" + "=" * 60)
    print("IQ問題追加スクリプト（第10弾・最終）")
    print("=" * 60)
    
    questions = []
    
    # 確率問題（101-110）
    print("[1/5] 確率問題を生成中...")
    for i in range(101, 111):
        number = (i - 100) % 6 + 1
        questions.append((
            f"サイコロを1回振って{number}が出る確率は？",
            f"images/iq_batch10_{i:03d}.svg",
            [
                {"id":"A","text":"1/6"},
                {"id":"B","text":"1/3"},
                {"id":"C","text":"1/2"},
                {"id":"D","text":"1/4"}
            ],
            [0],
            "確率",
            "2",
            8,
            "サイコロの基本確率",
            "確率計算"
        ))
    print(f"  ✓ 確率問題: 10問")
    
    # 組み合わせ問題（111-120）
    print("[2/5] 組み合わせ問題を生成中...")
    for i in range(111, 121):
        n = (i - 110) + 2
        combinations = n * (n - 1) // 2
        questions.append((
            f"{n}個から2個選ぶ組み合わせの数は？",
            f"images/iq_batch10_{i:03d}.svg",
            [
                {"id":"A","text":f"{combinations}通り"},
                {"id":"B","text":f"{combinations+1}通り"},
                {"id":"C","text":f"{combinations-1}通り"},
                {"id":"D","text":f"{n*2}通り"}
            ],
            [0],
            "組み合わせ",
            "3",
            12,
            f"{n}C2の計算",
            "組み合わせ計算"
        ))
    print(f"  ✓ 組み合わせ問題: 10問")
    
    # 推移律問題（121-130）
    print("[3/5] 推移律問題を生成中...")
    for i in range(121, 131):
        questions.append((
            f"A>B、B>Cのとき、AとCの関係は？",
            f"images/iq_batch10_{i:03d}.svg",
            [
                {"id":"A","text":"A>C"},
                {"id":"B","text":"A<C"},
                {"id":"C","text":"A=C"},
                {"id":"D","text":"不明"}
            ],
            [0],
            "論理",
            "2",
            8,
            "推移律の適用",
            "論理推論"
        ))
    print(f"  ✓ 推移律問題: 10問")
    
    # 面積問題（131-140）
    print("[4/5] 面積問題を生成中...")
    for i in range(131, 141):
        side = (i - 130) + 3
        area = side * side
        questions.append((
            f"一辺{side}cmの正方形の面積は？",
            f"images/iq_batch10_{i:03d}.svg",
            [
                {"id":"A","text":f"{area}cm²"},
                {"id":"B","text":f"{area+1}cm²"},
                {"id":"C","text":f"{area-1}cm²"},
                {"id":"D","text":f"{side*4}cm²"}
            ],
            [0],
            "図形",
            "2",
            8,
            "正方形の面積公式",
            "面積計算"
        ))
    print(f"  ✓ 面積問題: 10問")
    
    # 最終総合問題（141-149）
    print("[5/5] 最終総合問題を生成中...")
    for i in range(141, 150):
        problem_num = i - 140
        questions.append((
            f"🎉最終問題{problem_num}：3つの図形のパターンで次は？",
            f"images/iq_batch10_{i:03d}.svg",
            [
                {"id":"A","text":"円"},
                {"id":"B","text":"四角"},
                {"id":"C","text":"三角"},
                {"id":"D","text":"星"}
            ],
            [problem_num % 4],
            "総合",
            "4",
            20,
            "図形パターン総合",
            "最終問題"
        ))
    print(f"  ✓ 最終総合問題: 9問")
    
    # データベースに挿入
    print("\nデータベースに保存中...")
    for idx, q in enumerate(questions, 1):
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
        
        if idx % 10 == 0:
            print(f"  {idx}/49問 保存完了...")
    
    conn.commit()
    
    # 統計表示
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'IQ'")
    iq_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_count = cursor.fetchone()[0]
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("🎊🎊🎊 IQ問題500問達成！！！ 🎊🎊🎊")
    print("=" * 60)
    print(f"IQ問題数: {iq_count}問")
    print(f"全体問題数: {total_count}問")
    print("=" * 60)
    print("\n【達成した問題カテゴリ】")
    
    cursor = sqlite3.connect(DB_NAME).cursor()
    cursor.execute("""
        SELECT category, COUNT(*) as count 
        FROM questions 
        WHERE language = 'IQ' 
        GROUP BY category 
        ORDER BY count DESC
    """)
    categories = cursor.fetchall()
    
    for cat, count in categories:
        print(f"  {cat}: {count}問")
    
    print("\n" + "=" * 60)
    print("全10弾の追加が完了しました！")
    print("お疲れ様でした！🎉✨")
    print("=" * 60)

if __name__ == "__main__":
    add_iq_batch10_final()