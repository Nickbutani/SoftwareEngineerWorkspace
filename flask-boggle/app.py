from flask import Flask, session, redirect, url_for, request, render_template, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

boggle_game = Boggle()

@app.route('/')
def home():
    """Render homepage to start the game."""
    return render_template('home.html')

@app.route('/create-board', methods=['POST'])
def create_board():
    """Create a boggle board with the specified size."""
    try:
        size = int(request.form['size'])
    except (KeyError, ValueError, TypeError):
        return redirect(url_for('home')) # Redirect to home if the input is inappropriate
    
    print(size)
    board = boggle_game.make_board(size)
    
    session['board'] = board
    return redirect(url_for('index'))

@app.route('/board')
def index():
    """Display the Boggle board."""
    board = session.get('board', [])
    if not board:
        # Redirect home if no board is found in session
        return redirect(url_for('home'))
    return render_template('index.html', board=board)

@app.route('/check-word')
def check_word():
    word = request.args.get('word', '')
    board = session['board']
    print(board)
    print(word)
    response = {'result': boggle_game.check_valid_word(board, word)}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)