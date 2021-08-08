import requests
try:
    import secret
except ImportError: 
    #import env_secret as secret
    pass
import env_secret

class twilio():
    def __init__(self):
        self.account_sid = env_secret.twilio_sid
        self.auth_token = env_secret.twilio_token
        self.from_number = env_secret.twilio_number

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
        if twilio_client.account_sid == None:
            print("SID is None")
        if twilio_client.auth_token == None:
            print("Token is None")
        if twilio_client.from_number == None:
            print("From is None")
        pass

if __name__ == '__main__':
    test()

#cspell:ignore twilio
