import requests
try:
    import secret
except ImportError: 
    import env_secret as secret
#import secret

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
        self.r = requests.post(url, auth=(self.account_sid, self.auth_token), data=payload)
        return self.r

def test():
    twilio_client = twilio()
    twilio_client.send_message(secret.phone_number, 'Hello from Python!')
    print("twilio status ", twilio_client.r.status_code)
    if twilio_client.r.status_code != 201:
        #raise Exception('Bad status code from twilio')
        print(len(twilio_client.account_sid))
        print(len(twilio_client.auth_token))
        print(len(twilio_client.from_number))
        pass

if __name__ == '__main__':
    test()

#cspell:ignore twilio
