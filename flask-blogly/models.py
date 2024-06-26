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
    

class Tag(db.Model):
    """Tag."""

    __tablename__ = 'tags'

    def __repr__(self):
        """Show info about tag."""

        t = self
        return f"<Tag id={t.id} name={t.name}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    posts = db.relationship('Post', secondary='post_tags', backref='tags')

class PostTag(db.Model):
    """PostTag."""

    __tablename__ = 'post_tags'

    
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'),primary_key=True, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'),primary_key=True, nullable=False)
   
    def __init__(self, post_id, tag_id):
        self.post_id = post_id
        self.tag_id = tag_id