import requests
import secret

class AlphaVantage:
    def __init__(self):
        self.api_key = secret.alphavantage_key
        self.base_url = f'https://www.alphavantage.co/query?apikey={self.api_key}'

