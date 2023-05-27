from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/play', defaults={'x': 3, 'color': 'lightblue'})
@app.route('/play/<int:x>', defaults={'color': 'green'})
@app.route('/play/<int:x>/<string:color>')
def play(x, color):
    return render_template('index.html', num_boxes=x, color=color)
if __name__=="__main__":      
    app.run(debug=True)    