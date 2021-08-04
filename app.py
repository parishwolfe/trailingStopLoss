from flask import Flask, jsonfiy
from flask_basicauth import BasicAuth
import secret
from datetime import datetime
stocks = []
app = Flask(__name__)
from flask_apscheduler import APScheduler
app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


app.config['BASIC_AUTH_USERNAME'] = secret.username
app.config['BASIC_AUTH_PASSWORD'] = secret.password

basic_auth = BasicAuth(app)

def response_template(message):
    return jsonify({
        "user": secret.username,
        "time": datetime.now(),
        "message": message
    })


@app.route('/add')
@basic_auth.required
def add_ticker():
    
    
    global stocks
    stocks.append(ticker("a", "b"))
    return "hi!"

@app.route('/rm')
@basic_auth.required
def remove_ticker():
    global stocks
    for stock in stocks:
        if stock.ticker == "a":
            stocks.remove(stock)

@app.route('/notification_time')
def notification_time():
    return ""



class ticker():
    def __init__(self, name, percent, notif_number=None):
        self.ticker = name
        self.percent = percent
        self.notif_number = notif_number

def run_jobs():
    print("hi")
    pass

@app.route('/')
def index():
    return "See the documentation in the repo"

app.apscheduler.add_job(func=run_jobs, trigger='cron', id='0', minute="*", second="*/5") #day="", 
if __name__ == '__main__':
    app.run(port=8085, debug=False)

#cspell:ignore apscheduler notif jsonify