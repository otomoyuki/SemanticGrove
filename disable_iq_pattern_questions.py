import sqlite3
import json

DB_NAME = "SemanticGrove.db"

def disable_all_image_questions():
    """
    画像フィールドが存在するIQ問題をすべて一時無効化
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("=" * 70)
    print("IQ画像問題を一時無効化（改良版）")
    print("=" * 70)
    
    # 現在のIQ問題数を確認
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'IQ'")
    total_iq = cursor.fetchone()[0]
    print(f"\n現在のIQ問題数: {total_iq}問")
    
    # 画像問題を特定（question_jsonにimageフィールドがある）
    cursor.execute("""
        SELECT id, question_json 
        FROM questions 
        WHERE language = 'IQ'
    """)
    
    all_questions = cursor.fetchall()
    image_questions = []
    text_questions = []
    
    for q_id, q_json in all_questions:
        try:
            q_data = json.loads(q_json)
            if 'image' in q_data and q_data['image']:
                image_questions.append((q_id, q_data))
            else:
                text_questions.append((q_id, q_data))
        except:
            text_questions.append((q_id, {}))
    
    print(f"\n画像問題: {len(image_questions)}問")
    print(f"テキスト問題（数列など）: {len(text_questions)}問")
    
    if len(image_questions) == 0:
        print("\n✅ 画像問題は既に処理済みか、存在しません。")
        conn.close()
        return
    
    # 画像問題のIDリストを表示
    image_ids = [q[0] for q in image_questions]
    print(f"\n無効化する問題ID範囲: {min(image_ids)} ~ {max(image_ids)}")
    print(f"問題例:")
    for i, (q_id, q_data) in enumerate(image_questions[:3], 1):
        question_text = q_data.get('question', '')[:50]
        image_path = q_data.get('image', '')
        print(f"  {i}. ID{q_id}: {question_text}... (画像: {image_path})")
    
    # 画像問題を 'IQ_IMAGE_DISABLED' に変更
    placeholders = ','.join(['?' for _ in image_ids])
    cursor.execute(f"""
        UPDATE questions 
        SET language = 'IQ_IMAGE_DISABLED',
            usage = CASE 
                WHEN usage IS NULL THEN '[一時無効化: 選択肢画像準備中]'
                ELSE usage || ' [一時無効化: 選択肢画像準備中]'
            END
        WHERE id IN ({placeholders})
    """, image_ids)
    
    conn.commit()
    
    # 更新後の状況を確認
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'IQ'")
    active_iq = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM questions WHERE language = 'IQ_IMAGE_DISABLED'")
    disabled_iq = cursor.fetchone()[0]
    
    print("\n" + "=" * 70)
    print("✅ 処理完了")
    print("=" * 70)
    print(f"有効なIQ問題: {active_iq}問（数列問題など、テキストのみ）")
    print(f"無効化されたIQ問題: {disabled_iq}問（画像問題）")
    print(f"\n👉 画像問題は選択肢画像が準備でき次第、再度有効化します。")
    print("=" * 70)
    
    # 残っている問題のサンプル
    print("\n📋 有効なIQ問題のサンプル（最初の5問）:")
    for i, (q_id, q_data) in enumerate(text_questions[:5], 1):
        question_text = q_data.get('question', '')[:60]
        print(f"  {i}. {question_text}...")
    
    conn.close()

if __name__ == "__main__":
    disable_all_image_questions()