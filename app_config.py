"""
アプリケーション設定ファイル
開発環境: SQLite×2
本番環境: SQLite(問題) + PostgreSQL(ユーザー)
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """基本設定"""
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # SQLite（問題データ - 読み取り専用）
    SQLALCHEMY_DATABASE_URI = 'sqlite:///SemanticGrove.db'
    
    # PostgreSQL（ユーザーデータ）
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # Render対応（postgres:// を postgresql:// に変換）
    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    # ローカル開発環境では確実にSQLiteを使う
    SQLALCHEMY_BINDS = {
        'postgres': DATABASE_URL if DATABASE_URL else 'sqlite:///users.db'
    }
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(Config):
    """開発環境設定"""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # 開発環境では明示的にSQLiteを使う
    SQLALCHEMY_BINDS = {
        'postgres': 'sqlite:///users.db'
    }

class ProductionConfig(Config):
    """本番環境設定"""
    DEBUG = False
    SQLALCHEMY_ECHO = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}