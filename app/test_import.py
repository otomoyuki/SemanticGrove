try:
    from werkzeug.security import generate_password_hash
    print("✓ werkzeug インポート成功")
except ImportError as e:
    print(f"✗ werkzeug インポートエラー: {e}")

try:
    import sqlite3
    print("✓ sqlite3 インポート成功")
except ImportError as e:
    print(f"✗ sqlite3 インポートエラー: {e}")

try:
    import json
    print("✓ json インポート成功")
except ImportError as e:
    print(f"✗ json インポートエラー: {e}")

print("\nすべてのインポートが成功すれば、init_database.pyが動くはずです")