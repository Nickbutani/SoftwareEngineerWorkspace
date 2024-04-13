from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app

class User(db.Model):
    """User."""

    __tablename__ = 'users'

    def __repr__(self):
        """Show info about user."""

        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String, nullable=False, default="https://www.kindpng.com/picc/m/78-785827_user-profile-avatar-login")


class Post(db.Model):
    """Post."""

    __tablename__ = 'posts'

    def __repr__(self):
        """Show info about post."""

        p = self
        return f"<Post id={p.id} title={p.title} content={p.content} created_at={p.created_at} user_id={p.user_id}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='posts')
    
    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id
    

