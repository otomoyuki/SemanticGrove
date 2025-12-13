import sqlite3
import json
import os

DB_NAME = "SemanticGrove.db"
IMAGE_DIR = "static/images"

def generate_svg_pattern_1():
    """パターン1：色の交互パターン"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">次の色パターンで？に入るのは？</text>
  
  <!-- 3x3グリッド -->
  <rect x="80" y="80" width="60" height="60" fill="#ef4444" stroke="#333" stroke-width="2"/>
  <rect x="170" y="80" width="60" height="60" fill="#3b82f6" stroke="#333" stroke-width="2"/>
  <rect x="260" y="80" width="60" height="60" fill="#ef4444" stroke="#333" stroke-width="2"/>
  
  <rect x="80" y="170" width="60" height="60" fill="#3b82f6" stroke="#333" stroke-width="2"/>
  <rect x="170" y="170" width="60" height="60" fill="#ef4444" stroke="#333" stroke-width="2"/>
  <rect x="260" y="170" width="60" height="60" fill="#3b82f6" stroke="#333" stroke-width="2"/>
  
  <rect x="80" y="260" width="60" height="60" fill="#ef4444" stroke="#333" stroke-width="2"/>
  <rect x="170" y="260" width="60" height="60" fill="#3b82f6" stroke="#333" stroke-width="2"/>
  <text x="290" y="305" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">?</text>
</svg>'''

def generate_svg_pattern_2():
    """パターン2：図形の数が増える"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">図形の数のパターンは？</text>
  
  <!-- 1個 -->
  <circle cx="100" cy="120" r="20" fill="#10b981" stroke="#333" stroke-width="2"/>
  
  <!-- 2個 -->
  <circle cx="220" cy="120" r="20" fill="#10b981" stroke="#333" stroke-width="2"/>
  <circle cx="260" cy="120" r="20" fill="#10b981" stroke="#333" stroke-width="2"/>
  
  <!-- 3個 -->
  <circle cx="360" cy="120" r="20" fill="#10b981" stroke="#333" stroke-width="2"/>
  <circle cx="400" cy="120" r="20" fill="#10b981" stroke="#333" stroke-width="2"/>
  <circle cx="440" cy="120" r="20" fill="#10b981" stroke="#333" stroke-width="2"/>
  
  <!-- ? -->
  <text x="300" y="250" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">次は何個？</text>
</svg>'''

def generate_svg_pattern_3():
    """パターン3：形状の変化（丸→四角→三角）"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">次に来る図形は？</text>
  
  <circle cx="100" cy="150" r="40" fill="#f59e0b" stroke="#333" stroke-width="2"/>
  <rect x="210" y="110" width="80" height="80" fill="#8b5cf6" stroke="#333" stroke-width="2"/>
  <polygon points="400,110 440,190 360,190" fill="#ec4899" stroke="#333" stroke-width="2"/>
  
  <text x="300" y="300" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">?</text>
</svg>'''

def generate_svg_pattern_4():
    """パターン4：回転（時計回り）"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">矢印の向きのパターンは？</text>
  
  <!-- 上 -->
  <g transform="translate(100, 120)">
    <polygon points="0,-30 15,10 -15,10" fill="#14b8a6" stroke="#333" stroke-width="2"/>
  </g>
  
  <!-- 右 -->
  <g transform="translate(240, 120)">
    <polygon points="30,0 -10,15 -10,-15" fill="#14b8a6" stroke="#333" stroke-width="2"/>
  </g>
  
  <!-- 下 -->
  <g transform="translate(380, 120)">
    <polygon points="0,30 15,-10 -15,-10" fill="#14b8a6" stroke="#333" stroke-width="2"/>
  </g>
  
  <text x="300" y="280" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">?</text>
</svg>'''

def generate_svg_pattern_5():
    """パターン5：大きさの変化"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">円の大きさのパターンは？</text>
  
  <circle cx="80" cy="150" r="20" fill="#06b6d4" stroke="#333" stroke-width="2"/>
  <circle cx="180" cy="150" r="30" fill="#06b6d4" stroke="#333" stroke-width="2"/>
  <circle cx="300" cy="150" r="40" fill="#06b6d4" stroke="#333" stroke-width="2"/>
  
  <text x="460" y="160" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">?</text>
</svg>'''

def generate_svg_pattern_6():
    """パターン6：対称パターン"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">左右対称を完成させるには？</text>
  
  <!-- 左側 -->
  <circle cx="150" cy="120" r="25" fill="#f43f5e" stroke="#333" stroke-width="2"/>
  <rect x="120" y="180" width="60" height="60" fill="#3b82f6" stroke="#333" stroke-width="2"/>
  
  <!-- 中央線 -->
  <line x1="300" y1="80" x2="300" y2="280" stroke="#999" stroke-width="2" stroke-dasharray="5,5"/>
  
  <!-- 右側（一部） -->
  <circle cx="450" cy="120" r="25" fill="#f43f5e" stroke="#333" stroke-width="2"/>
  
  <text x="450" y="220" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">?</text>
</svg>'''

def generate_svg_pattern_7():
    """パターン7：重なりのパターン"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">重なりの数のパターンは？</text>
  
  <!-- 重なり1 -->
  <circle cx="80" cy="140" r="30" fill="#84cc16" opacity="0.7" stroke="#333" stroke-width="2"/>
  <circle cx="110" cy="140" r="30" fill="#84cc16" opacity="0.7" stroke="#333" stroke-width="2"/>
  
  <!-- 重なり2 -->
  <circle cx="220" cy="140" r="30" fill="#eab308" opacity="0.7" stroke="#333" stroke-width="2"/>
  <circle cx="250" cy="140" r="30" fill="#eab308" opacity="0.7" stroke="#333" stroke-width="2"/>
  <circle cx="280" cy="140" r="30" fill="#eab308" opacity="0.7" stroke="#333" stroke-width="2"/>
  
  <text x="420" y="150" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">?</text>
</svg>'''

def generate_svg_pattern_8():
    """パターン8：分割パターン"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">図形の分割パターンは？</text>
  
  <!-- 2分割 -->
  <rect x="60" y="100" width="80" height="80" fill="#a78bfa" stroke="#333" stroke-width="2"/>
  <line x1="100" y1="100" x2="100" y2="180" stroke="#333" stroke-width="3"/>
  
  <!-- 4分割 -->
  <rect x="200" y="100" width="80" height="80" fill="#a78bfa" stroke="#333" stroke-width="2"/>
  <line x1="240" y1="100" x2="240" y2="180" stroke="#333" stroke-width="3"/>
  <line x1="200" y1="140" x2="280" y2="140" stroke="#333" stroke-width="3"/>
  
  <text x="420" y="150" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">?</text>
</svg>'''

def generate_svg_pattern_9():
    """パターン9：点の増加"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">サイコロの目のパターンは？</text>
  
  <!-- 1 -->
  <rect x="60" y="100" width="80" height="80" fill="white" stroke="#333" stroke-width="2"/>
  <circle cx="100" cy="140" r="6" fill="#333"/>
  
  <!-- 2 -->
  <rect x="180" y="100" width="80" height="80" fill="white" stroke="#333" stroke-width="2"/>
  <circle cx="200" cy="120" r="6" fill="#333"/>
  <circle cx="240" cy="160" r="6" fill="#333"/>
  
  <!-- 3 -->
  <rect x="300" y="100" width="80" height="80" fill="white" stroke="#333" stroke-width="2"/>
  <circle cx="320" cy="120" r="6" fill="#333"/>
  <circle cx="340" cy="140" r="6" fill="#333"/>
  <circle cx="360" cy="160" r="6" fill="#333"/>
  
  <text x="480" y="150" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">?</text>
</svg>'''

def generate_svg_pattern_10():
    """パターン10：グラデーション変化"""
    return '''<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#000;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fff;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <text x="300" y="30" font-size="18" font-weight="bold" text-anchor="middle" fill="#333">濃淡のパターンは？</text>
  
  <circle cx="100" cy="150" r="40" fill="#000" stroke="#333" stroke-width="2"/>
  <circle cx="220" cy="150" r="40" fill="#666" stroke="#333" stroke-width="2"/>
  <circle cx="340" cy="150" r="40" fill="#ccc" stroke="#333" stroke-width="2"/>
  
  <text x="480" y="160" font-size="48" font-weight="bold" text-anchor="middle" fill="#666">?</text>
</svg>'''

def create_svg_files():
    """SVGファイルを生成"""
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    
    svg_generators = [
        generate_svg_pattern_1,
        generate_svg_pattern_2,
        generate_svg_pattern_3,
        generate_svg_pattern_4,
        generate_svg_pattern_5,
        generate_svg_pattern_6,
        generate_svg_pattern_7,
        generate_svg_pattern_8,
        generate_svg_pattern_9,
        generate_svg_pattern_10,
    ]
    
    print("=" * 60)
    print("SVGファイル生成中...")
    print("=" * 60)
    
    for i, generator in enumerate(svg_generators, 1):
        filename = f"iq_batch8_{i:03d}.svg"
        filepath = os.path.join(IMAGE_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(generator())
        
        print(f"✓ {filename}")
    
    print(f"\n✓ {len(svg_generators)}個のSVGファイルを作成しました")

def add_iq_batch8_part1():
    """IQ問題追加（第8弾・前半10問）"""
    
    # まずSVGファイルを生成
    create_svg_files()
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("\n" + "=" * 60)
    print("IQ問題追加スクリプト（第8弾・前半10問）")
    print("=" * 60)
    
    questions = [
        ("次の色パターンで？に入るのは？",
         "images/iq_batch8_001.svg",
         [{"id":"A","text":"赤"},{"id":"B","text":"青"},{"id":"C","text":"黄"},{"id":"D","text":"緑"}],
         [0], "図形パターン", "2", 8, "市松模様パターン", "色の交互配置"),
        
        ("図形の数のパターンで次に来るのは？",
         "images/iq_batch8_002.svg",
         [{"id":"A","text":"3個"},{"id":"B","text":"4個"},{"id":"C","text":"5個"},{"id":"D","text":"6個"}],
         [1], "図形パターン", "2", 8, "1,2,3,4と増加", "数の規則性"),
        
        ("次に来る図形は？",
         "images/iq_batch8_003.svg",
         [{"id":"A","text":"円"},{"id":"B","text":"四角"},{"id":"C","text":"三角"},{"id":"D","text":"星"}],
         [0], "図形パターン", "2", 8, "円→四角→三角→円の繰り返し", "形状の循環"),
        
        ("矢印の向きのパターンで次は？",
         "images/iq_batch8_004.svg",
         [{"id":"A","text":"上"},{"id":"B","text":"右"},{"id":"C","text":"下"},{"id":"D","text":"左"}],
         [3], "回転", "3", 10, "時計回りに90度回転", "回転パターン"),
        
        ("円の大きさのパターンで次は？",
         "images/iq_batch8_005.svg",
         [{"id":"A","text":"r=40"},{"id":"B","text":"r=50"},{"id":"C","text":"r=60"},{"id":"D","text":"r=45"}],
         [1], "図形パターン", "3", 10, "半径が10ずつ増加", "大きさの規則"),
        
        ("左右対称を完成させるには？",
         "images/iq_batch8_006.svg",
         [{"id":"A","text":"円"},{"id":"B","text":"四角"},{"id":"C","text":"三角"},{"id":"D","text":"星"}],
         [1], "対称", "3", 12, "鏡像関係", "対称性認識"),
        
        ("重なりの数のパターンは？",
         "images/iq_batch8_007.svg",
         [{"id":"A","text":"3個"},{"id":"B","text":"4個"},{"id":"C","text":"5個"},{"id":"D","text":"6個"}],
         [1], "図形パターン", "3", 12, "2,3,4と増加", "個数パターン"),
        
        ("図形の分割パターンで次は？",
         "images/iq_batch8_008.svg",
         [{"id":"A","text":"6分割"},{"id":"B","text":"8分割"},{"id":"C","text":"9分割"},{"id":"D","text":"16分割"}],
         [1], "図形パターン", "4", 15, "2,4,8と倍増", "分割規則"),
        
        ("サイコロの目のパターンで次は？",
         "images/iq_batch8_009.svg",
         [{"id":"A","text":"3"},{"id":"B","text":"4"},{"id":"C","text":"5"},{"id":"D","text":"6"}],
         [1], "図形パターン", "2", 8, "1,2,3,4と増加", "連続パターン"),
        
        ("濃淡のパターンで次は？",
         "images/iq_batch8_010.svg",
         [{"id":"A","text":"白"},{"id":"B","text":"薄灰"},{"id":"C","text":"灰"},{"id":"D","text":"黒"}],
         [0], "図形パターン", "3", 10, "黒→灰→薄灰→白", "明度変化"),
    ]
    
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
    print("✓ IQ問題追加完了（第8弾・前半10問）！")
    print("=" * 60)
    print(f"IQ問題数: {iq_count}問")
    print(f"全体問題数: {total_count}問")
    print(f"目標500問まで残り: {max(0, 500 - iq_count)}問")
    print("=" * 60)

if __name__ == "__main__":
    add_iq_batch8_part1()