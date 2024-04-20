from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=1, max=20)], render_kw ={"autocomplete": "off"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)],render_kw ={"autocomplete": "off"})
    email = StringField('Email', validators=[InputRequired(), Email(), Length(min=1, max=50)])
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1, max=30)])
    submit = StringField('Submit')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=1, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)])
    submit = StringField('Submit')
    
class FeedbackForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(min=1, max=100)])
    content = StringField('Content', validators=[InputRequired(), Length(min=1, max=300)])
    submit = StringField('Submit')
    
    