#########################################
#   Trailing Stop Loss Notifier         #
#   Author: Parish Wolfe                #
#   Vanderbilt University               #
#########################################
#requires python version 3.7+

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
import alphavantage
import twilio
phone_number = secret.phone_number

app.config['JSON_SORT_KEYS'] = False
app.config['BASIC_AUTH_USERNAME'] = secret.username
app.config['BASIC_AUTH_PASSWORD'] = secret.password

#basic_auth = BasicAuth(app)

def response_template(message):
    return jsonify({
        "user": secret.username,
        "time": datetime.now(),
        "message": message
    })


@app.route('/add', methods=['POST'])
#@basic_auth.required
def add_ticker():
    global stocks
    if len(stocks) > 3:
        return response_template("Too many stocks, remove a stock first"), 400
    ticker = request.args.get('ticker')
    if ticker is None:
        return response_template("No ticker provided"), 400
    if ticker in stocks:
        return response_template("Ticker already exists"), 400
    percent = request.args.get('percent')
    if percent is None:
        return response_template("No percent provided"), 400
    if not percent.isdigit():
        return response_template("Percent not a number"), 400
    percent = int(percent)
    if percent < 1 or percent > 100:
        return response_template("Percent not between 1 and 100"), 400
    stocks.append(stock(ticker, percent))
    return response_template(f"Added stock {ticker}")

@app.route('/rm', methods=['POST'])
#@basic_auth.required
def remove_ticker():
    global stocks
    ticker = request.args.get('ticker')
    for stock in stocks:
        if stock.ticker == ticker:
            stocks.remove(stock)
            return response_template(f"Removed stock {ticker}")
        else:
            return response_template(f"Ticker {ticker} not found"), 404

@app.route('/ls', methods=['GET'])
#@basic_auth.required
def list_stocks():
    global stocks
    if len(stocks) == 0:
        return response_template("No stocks")
    return response_template(f"{stocks}")

@app.route('/settings', methods=["POST"])
#@basic_auth.required
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
        else:
            global phone_number
            phone_number = "+1" + phone
    if h == None and m == None and d == None and phone == None:
        return response_template("No settings to update"), 200
    global job_version
    app.apscheduler.remove_job(id=job_version)
    job_version = str(int(job_version) + 1)

    app.apscheduler.add_job(func=run_jobs, trigger='cron', hour=h, minute=m, day=d, id=job_version)
    return response_template("Settings updated"), 200


class stock():
    def __init__(self, name, percent):
        self.ticker = name
        self.percent = percent * 0.01
        self.high_close = 0

def run_jobs():
    global stocks
    message = None
    for stock in stocks:
        new_daily = alphavantage.daily(stock.ticker)
        new_daily.get_data()
        if new_daily.r.status_code != 200:
            #TODO message error
            pass
        else:
            if new_daily.get_daily_data()[0].get("4. close") > stock.high_close:
                stock.high_close = new_daily.get_daily_data()[0].get("4. close")
                #message = f"{stock.ticker} is at {stock.high_close} today"
            else:
                decrease = stock.high_close - new_daily.get_daily_data()[0].get("4. close")
                percent_decrease = (decrease / stock.high_close) * 100
                if percent_decrease > stock.percent:
                    message += f"{stock.ticker} is at {stock.high_close} today, {percent_decrease}% decrease\n"
    if message != None:
        global phone_number
        notification = twilio.twilio()
        notification.send_message(phone_number, "Urgent stock notification!!\n" + message)
    
    


@app.route('/')
def index():
    return "See the documentation in the repo"

app.apscheduler.add_job(func=run_jobs, trigger='cron', id=job_version, day="*", hour="4", minute="15") #second=None, minute="*" #day="*", hour="*", minute="*"
if __name__ == '__main__':
    app.run(port=8085, debug=True)

#cspell:ignore apscheduler notif jsonify twilio isdigit