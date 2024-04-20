from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)
    

class User(db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text(), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text(), nullable=False, unique=True)
    first_name = db.Column(db.Text(), nullable=False)
    last_name = db.Column(db.Text(), nullable=False)

    
    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        password_str = password.decode('utf-8')
        user = cls(username=username, password=password_str, email=email, first_name=first_name, last_name=last_name)
        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return user
        else:
            return False
        
    
class Feedback(db.Model):
    
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    username = db.Column(db.Text(), db.ForeignKey('users.username'), nullable=False)
    
    user = db.relationship('User', backref='feedback')
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'username': self.username
        }
    
    @classmethod
    def create_feedback(cls, title, content, username):
        feedback = cls(title=title, content=content, username=username)
        db.session.add(feedback)
        return feedback