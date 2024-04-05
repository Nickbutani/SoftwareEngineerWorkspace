from flask import Flask, request, render_template
from stories import story as madlibs_story 
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/form')
def form():
    prompts = madlibs_story.prompts 
    return render_template('form.html', prompts=prompts)

@app.route('/story', methods=["POST"])
def generate_story():
    
    answers = {prompt: request.form[prompt] for prompt in madlibs_story.prompts} 
    generated_story = madlibs_story.generate(answers)  
    return render_template('story.html', generated_story=generated_story)