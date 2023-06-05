from flask import Flask, render_template, redirect, url_for,session

app = Flask(__name__)
app.secret_key = '100500'

@app.route('/')
def index():
    session['count'] = session.get('count',0)
    return render_template('index.html', count=session['count'])

@app.route('/increment')
def increment():
    session['count'] = session.get('count', 0) + 2
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect(url_for('index'))

@app.route('/destroy_session')
def destroy_session():
    session.pop('count', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
