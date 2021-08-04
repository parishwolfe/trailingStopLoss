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

{
    "user": null,
    "time": "Wed, 04 Aug 2021 14:47:03 GMT",
    "message": "UPRO"
}

### POST {url}/settings

### parameters

Times represent when the application collects stock data and sends it to the phone nubmer.

- hour optional, modify hour of execution
- minute optional, modify minute of execution
- day, optional, modify day of execution, can be * to represent every day
- phone, optional, modify 10 digit US phone number to send notifications

## Configuration

### Settings

The default trigger is for 4:15 just after the stock market closes. These times are in local time.

### Environment Variables

environment variables should be created for the following configuration items. 

1. TW_SID = Your twilio SID
2. TW_TOKEN = Your twilio Token
3. TW_NUMBER = Your twilio phone number (with +1)
4. PHONE_NUMBER = Your target phone number
5. USERNAME = username for basic auth, commented by default (interfering with unit tests)
6. PASSWORD = password for basic auth, commented by default (interfering with unit tests)

