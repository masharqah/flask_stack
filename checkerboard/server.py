from flask import Flask, render_template

app=Flask(__name__)

@app.route('/', defaults={'r': 8, 'c': 8})
@app.route('/<int:r>', defaults={'c': 8})
@app.route('/<int:c>/<int:r>')
def Checkerboard(r,c):
    return render_template("checkerboard.html", x=r, y=c )

if __name__== "__main__":
    app.run(debug=True)
