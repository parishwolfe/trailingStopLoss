from flask import Flask, jsonify, request
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
job_version = str(1)


app.config['BASIC_AUTH_USERNAME'] = secret.username
app.config['BASIC_AUTH_PASSWORD'] = secret.password

#basic_auth = BasicAuth(app)

def response_template(message):
    return jsonify({
        "user": secret.username,
        "time": datetime.now(),
        "message": message
    })


@app.route('/add')
#@basic_auth.required
def add_ticker():
    global stocks
    if len(stocks) > 3:
        return response_template("Too many stocks, remove a stock first")
    
    
    stocks.append(ticker("a", "b"))
    return "hi!"

@app.route('/rm')
#@basic_auth.required
def remove_ticker():
    global stocks
    for stock in stocks:
        if stock.ticker == "a":
            stocks.remove(stock)

@app.route('/settings', methods=["POST"])
def settings():
    h = request.args.get("hour")
    m = request.args.get("minute")
    d = request.args.get("day")
    phone = request.args.get("phone")
    if d != None and d != "*":
        if not int(d) > 0 or not int(d) < 32:
            return response_template("Invalid day"), 400
    if h != None:
        if not int(h) > 0 or not int(h) < 24:
            return response_template("Invalid hour"), 400
    if m != None:
        if not int(m) >= 0 or not int(m) < 60:
            return response_template("Invalid minute"), 400
    if phone != None:
        if not phone.isdigit() or len(phone) != 10:
            return response_template("Invalid phone")
    if h == None and m == None and d == None and phone == None:
        return response_template("No settings to update"), 200
    global job_version
    app.apscheduler.remove_job(id=job_version)
    job_version = str(int(job_version) + 1)

    app.apscheduler.add_job(func=run_jobs, trigger='cron', hour=h, minute=m, day=d, id=job_version)
    return response_template("Settings updated"), 200



class ticker():
    def __init__(self, name, percent):
        self.ticker = name
        self.percent = percent


def run_jobs():
    print("hi")
    pass

@app.route('/')
def index():
    return "See the documentation in the repo"

app.apscheduler.add_job(func=run_jobs, trigger='cron', id=job_version, second=None, minute="*") #day="*", hour="*", minute="*"
if __name__ == '__main__':
    app.run(port=8085, debug=True)

#cspell:ignore apscheduler notif jsonify