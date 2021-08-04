import os

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

alphavantage_key = os.environ.get("AV_KEY")

twilio_sid = os.environ.get("TW_SID")
twilio_token = os.environ.get("TW_TOKEN")
twilio_number = "+1" + os.environ.get("TW_NUMBER")

phone_number = "+1" + os.environ.get("PHONE_NUMBER")