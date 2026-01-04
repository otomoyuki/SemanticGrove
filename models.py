from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """ユーザーテーブル（JWT認証対応版）"""
    __tablename__ = 'users'
    __bind_key__ = 'postgres'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)  # 追加
    password_hash = db.Column(db.String(255), nullable=True)  # 追加
    session_id = db.Column(db.String(200), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_active = db.Column(db.DateTime, default=datetime.utcnow)
    sg_points = db.Column(db.Integer, default=0)
    last_login_date = db.Column(db.Date, nullable=True)
    total_logins = db.Column(db.Integer, default=0)

    # リレーション
    history = db.relationship('QuestionHistory', backref='user', lazy=True, cascade='all, delete-orphan')
    stats = db.relationship('UserStats', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'

class QuestionHistory(db.Model):
    """問題ごとの詳細履歴"""
    __tablename__ = 'question_history'
    __bind_key__ = 'postgres'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # 問題情報（SQLiteのquestion.idを参照）
    question_id = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(100))
    difficulty = db.Column(db.String(20))
    mode = db.Column(db.String(20), nullable=False)  # 'beginner', 'intermediate', 'advanced'
    
    # 統計
    correct_count = db.Column(db.Integer, default=0)
    wrong_count = db.Column(db.Integer, default=0)
    total_count = db.Column(db.Integer, default=0)
    
    # タイムスタンプ
    first_attempted = db.Column(db.DateTime, default=datetime.utcnow)
    last_attempted = db.Column(db.DateTime, default=datetime.utcnow)
    
    # インデックス（検索高速化）
    __table_args__ = (
        db.Index('idx_user_question_mode', 'user_id', 'question_id', 'mode'),
        db.Index('idx_user_language_mode', 'user_id', 'language', 'mode'),
    )
    
    @property
    def accuracy_rate(self):
        """正答率を計算"""
        if self.total_count == 0:
            return 0.0
        return round((self.correct_count / self.total_count) * 100, 1)
    
    def __repr__(self):
        return f'<QuestionHistory user={self.user_id} q={self.question_id} mode={self.mode}>'

class UserStats(db.Model):
    """言語・モード別の集計統計"""
    __tablename__ = 'user_stats'
    __bind_key__ = 'postgres'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    language = db.Column(db.String(50), nullable=False)
    mode = db.Column(db.String(20), nullable=False)
    
    # 集計データ
    total_questions_attempted = db.Column(db.Integer, default=0)
    total_correct = db.Column(db.Integer, default=0)
    total_wrong = db.Column(db.Integer, default=0)
    accuracy_rate = db.Column(db.Float, default=0.0)
    
    # タイムスタンプ
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # ユニーク制約
    __table_args__ = (
        db.UniqueConstraint('user_id', 'language', 'mode', name='unique_user_language_mode'),
        db.Index('idx_user_stats', 'user_id', 'language', 'mode'),
    )
    
    def update_stats(self):
        """統計を再計算"""
        if self.total_questions_attempted > 0:
            self.accuracy_rate = round((self.total_correct / self.total_questions_attempted) * 100, 1)
        else:
            self.accuracy_rate = 0.0
    
    def __repr__(self):
        return f'<UserStats user={self.user_id} {self.language} {self.mode}>'
    

class PointHistory(db.Model):
    """SGポイント履歴"""
    __tablename__ = 'point_history'
    __bind_key__ = 'postgres'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    points = db.Column(db.Integer, nullable=False)  # +10, -5 など
    reason = db.Column(db.String(100), nullable=False)  # 'question_correct', 'feedback', etc
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<PointHistory {self.user_id}: {self.points} ({self.reason})>'


class Feedback(db.Model):
    """フィードバック（ご意見）"""
    __tablename__ = 'feedback'
    __bind_key__ = 'postgres'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)  # 'bug', 'feature', 'other'
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='new')  # 'new', 'reviewed', 'resolved'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Feedback {self.id}: {self.category} ({self.status})>'