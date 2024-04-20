from flask import Flask, render_template, request, redirect, session
from models import db, User, connect_db, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm
import bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'this is a secret key'

connect_db(app)

with app.app_context():
    db.create_all()
    
    
@app.route('/')
def home():
    return redirect('/register')

@app.route('/register', methods=['GET'])
def register():
    form = RegisterForm()
    
    return render_template('register.html', form=form)

@app.route('/register', methods=['POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User.register(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        db.session.add(user)
        db.session.commit()
        
        return redirect('/login')
    else:
        session['user'] = None
        return render_template('register.html', form=form)

@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    user = session.get('user')
    return render_template('login.html', user=user, form=form)

@app.route('/login', methods=['POST'])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)
        if user:
            session['user'] = user.username
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors = ['Invalid username/password']
            return render_template('login.html', user=user, form=form)
    else:
        return render_template('login.html', user=user, form=form)
    
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')
    

    

@app.route('/users/<username>', methods=['GET'])
def user(username):
    user = User.query.filter_by(username=username).first()
    feedback = Feedback.query.filter_by(username=username).all()
    form = FeedbackForm()
    return render_template('user.html', user=user, feedback=feedback, form=form)

@app.route('/users/<username>/delete', methods=['POST'])
def delete_user(username):
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()
    return redirect('/login')

@app.route('/users/<username>/feedback/add', methods=['GET'])
def add_feedback(username):
    form = FeedbackForm()
    user = User.query.filter_by(username=username).first()
    return render_template('add_feedback.html', user=user, form=form)

@app.route('/users/<username>/feedback/add', methods=['POST'])
def add_feedback_post(username):
    title = request.form['title']
    content = request.form['content']
    feedback = Feedback.create_feedback(title, content, username)
    db.session.add(feedback)
    db.session.commit()
    return redirect(f'/users/{username}')

@app.route('/feedback/<int:id>/update', methods=['GET'])
def update_feedback(id):
    user = session.get('user')
    feedback = Feedback.query.get(id)
    form = FeedbackForm(obj=feedback)
    return render_template('update_feedback.html', feedback=feedback, user=user, form=form)

@app.route('/feedback/<int:id>/update', methods=['POST'])
def update_feedback_post(id):
    feedback = Feedback.query.get(id)
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data
        db.session.commit()  # Commit changes to the database
        return redirect(f'/users/{feedback.username}')
    return render_template('update_feedback.html', feedback=feedback, form=form)

@app.route('/feedback/<int:id>/delete', methods=['POST'])
def delete_feedback(id):
    feedback = Feedback.query.get_or_404(id)
    db.session.delete(feedback)
    db.session.commit()
    return redirect(f'/users/{feedback.username}')
