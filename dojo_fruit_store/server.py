from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    menu =request.form
    print (menu)
    total = int(menu['strawberry'])+int(menu['raspberry'])+int(menu['apple'])
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template ("checkout.html",menu=menu, total=total, dt=dt)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    