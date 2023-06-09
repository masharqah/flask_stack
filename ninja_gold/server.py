from flask import Flask, render_template, request, session, redirect, url_for
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key='100200'
@app.route('/')
def index():
    if "gold" not in session :
        session['gold']=0
        session['tracker']=[]    
        session['counter']=15
        session['status']='none'
    gold=session['gold']
    tracker=session['tracker']
    staus=session['status']
    counter=session['counter']
    return render_template('index.html', gold=gold, tracker=tracker, staus=staus, counter=counter)

@app.route('/reset', methods=['POST'])
def reset ():
    session['gold']=0
    session['counter']=15
    session['tracker']=[] 
    return redirect ("/")

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        amount=random.randint(10,20)
        logger=datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
        trackMessage = f"you earned {amount} from {request.form['building']} at {logger} "
    
    elif request.form['building'] == 'cave':
        amount=random.randint(5,10)
        logger=datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
        trackMessage = f"you earned {amount} from {request.form['building']} at {logger} "

    elif request.form['building'] == 'house':
        amount=random.randint(2,5)
        logger=datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
        trackMessage = f"you earned {amount} from {request.form['building']} at {logger} "

    elif request.form['building'] == 'casino':
        amount=random.randint(-50,50)
        logger=datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
        if amount < 0 :
            trackMessage = f"you lost {amount} from {request.form['building']} at {logger} Gambler!"
        elif amount > 0 :
            trackMessage = f"you earned {amount} from {request.form['building']} at {logger} "
        elif amount == 0 :
            trackMessage = f"{request.form['building']} is not giving neither taking from you ...{logger} "
    
    session['tracker'].append(trackMessage)
    session["gold"]+=amount
    session['counter']-=1

    return redirect ("/")
  

 

if __name__ == '__main__':
    app.run(debug=True)