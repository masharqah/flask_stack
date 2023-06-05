from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = '200300'

@app.route('/', methods=['GET', 'POST'])
def game():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)

    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess < session['number']:
            message = 'Too low!'
        elif guess > session['number']:
            message = 'Too high!'
        else:
            message = 'Congratulations! You guessed the correct number!'
            session.pop('number')
        return render_template('game.html', message=message)

    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)
