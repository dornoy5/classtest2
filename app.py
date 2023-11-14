from flask import Flask, request, render_template
from flask_cors import CORS
from tools.numbers.simp import add_numbers, subtract_numbers
from tools.numbers.comp import sumofdigits, ispal

app = Flask(__name__)
CORS(app)
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        a = request.form.get('a', type=float)
        b = request.form.get('b', type=float)
        result = add_numbers(a, b)
        return f'Result of adding {b} to {a} is {result}'
    return render_template('index.html')

@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
    if request.method == 'POST':
        a = request.form.get('a', type=float)
        b = request.form.get('b', type=float)
        result = subtract_numbers(a, b)
        return f'Result of subtracting {b} from {a} is {result}'
    return render_template('index.html')

@app.route('/sumofdigits', methods=['GET', 'POST'])
def sum_digits():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        result= sumofdigits(number)
        return f'Result of sum of digits is {result}'
    return render_template('index.html')

@app.route('/ispal', methods=['GET', 'POST'])
def is_palindrome():
    if request.method == 'POST':
        number = int(request.form['number'])
        return str(ispal(number))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
