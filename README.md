# trailingStopLoss

This is a flask app that uses twilio and alphavantage apis to calculate a trailing stop loss on up to three stocks that you supply via the endpoints. 

## Endpoints

### POST {url}/add
### parameters
- ticker required, must be a valid ticker symbol. 
- percent required, whole digit number representing a percentage for the trailing stop loss notification

{
    "user": "admin",
    "time": "Wed, 04 Aug 2021 01:13:01 GMT",
    "message": "Added stock UPRO"
}

### POST {url}/rm
### parameters
- ticker required, ticker symbol to remove from list

{
    "user": "admin",
    "time": "Wed, 04 Aug 2021 01:13:01 GMT",
    "message": "Removed stock UPRO"
}

### GET {url}/ls
Returns the list of stocks that the application is monitoring

### POST {url}/settings
### parameters
Times represent when the application collects stock data and sends it to the phone nubmer.
- hour optional, modify hour of execution
- minute optional, modify minute of execution
- day, optional, modify day of execution, can be * to represent every day
- phone, optional, modify 10 digit US phone number to send notifications

## defaults
### secret file
defaults are set using a secrets file. A plain text file named secret.py should be created in the project root. 
several configuration items need to be inserted 
1. twilio_sid = Your twilio SID
2. twilio_token = Your twilio Token
3. twilio_number = Your twilio phone number (with +1)
4. phone_number = Your target phone number
5. username = username for basic auth, commented by default (interfering with unit tests)
6. password = password for basic auth, commented by default (interfering with unit tests)

