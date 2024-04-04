# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a, b))

@app.route('/sub')
def sub_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a, b))

@app.route('/mult')
def mult_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a, b))

@app.route('/div')
def div_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a, b))

@app.route('/math/<operation>')
def math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    if operation == 'add':
        return str(add(a, b))
    elif operation == 'sub':
        return str(sub(a, b))
    elif operation == 'mult':
        return str(mult(a, b))
    elif operation == 'div':
        return str(div(a, b))
    else:
        return 'Invalid operation'