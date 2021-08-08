import os

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

alphavantage_key = os.getenv("AV_KEY")

twilio_sid = os.getenv("TW_SID")
twilio_token = os.getenv("TW_TOKEN")
twilio_number = os.getenv("TW_NUMBER")

phone_number = os.getenv("PHONE_NUMBER")

print("test", os.getenv("secrets.TEST"))
for k, v in os.environ.items():
    print(k)

#cspell:ignore getenv twilio
