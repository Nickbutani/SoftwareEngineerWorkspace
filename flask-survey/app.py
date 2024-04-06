from flask import Flask, request, jsonify, render_template, redirect, session, flash
from surveys import satisfaction_survey, personality_quiz
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SECRET_KEY']="oh-so-secret"


debug = DebugToolbarExtension(app)


responses = []



@app.route('/')
def home():
    return render_template('start.html', survey_title=satisfaction_survey.title, instructions=satisfaction_survey.instructions)

@app.route('/start_survey', methods=['POST'])
def start_survey():
    session['responses'] = []
    return redirect('/questions/1')

@app.route('/questions/<int:question_index>', methods=['GET', 'POST'])
def question(question_index):
    responses = session.get('responses', [])
    
    adjusted_index = question_index - 1

    if len(responses) == len(satisfaction_survey.questions):
        return redirect('/thanks')

    if question_index != len(responses) + 1:
        correct_next_index = len(responses) + 1
        flash(f"Invalid question index. Please answer question {correct_next_index}")
        return redirect(f'/questions/{correct_next_index}')

    if request.method == 'POST':
        answer = request.form.get('answer')
        responses.append(answer)
        session['responses'] = responses

        return redirect(f'/questions/{question_index + 1}')

    if adjusted_index < len(satisfaction_survey.questions):
        question = satisfaction_survey.questions[adjusted_index]
        return render_template('question.html', question=question, question_index=question_index)
    else:
        return redirect('/thanks')



@app.route('/answer', methods=["POST"])
def handle_answer():
    choice = request.form['choice']

    
    responses = session.get('responses', [])
    responses.append(choice)
    session['responses'] = responses

    if len(responses) < len(satisfaction_survey.questions):
        return redirect(f'/questions/{len(responses)}')
    else:
        return redirect('/thanks')
    
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

