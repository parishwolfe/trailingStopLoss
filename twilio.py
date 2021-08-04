import requests
import env_secret

class twilio():
    def __init__(self):
        self.account_sid = secret.twilio_sid
        self.auth_token = secret.twilio_token
        self.from_number = secret.twilio_number

    def send_message(self, to_number, message):
        url = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json'.format(self.account_sid)
        payload = {
            'From': self.from_number,
            'To': to_number,
            'Body': message
        }
        return requests.post(url, auth=(self.account_sid, self.auth_token), data=payload)

def test():
    twilio_client = twilio()
    twilio_client.send_message(secret.phone_number, 'Hello from Python!')

if __name__ == '__main__':
    test()

#cspell:ignore twilio
