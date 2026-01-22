#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''Returns the h1 title for the application'''
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    '''Prints the parameter to console and displays it in the browser'''
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    '''Displays all numbers in the range of the parameter on separate lines'''
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    '''Performs mathematical operations on two numbers'''
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
