import requests
import secret

class AlphaVantage:
    def __init__(self):
        self.api_key = secret.alphavantage_key
        self.base_url = f'https://www.alphavantage.co/query?apikey={self.api_key}'

class daily(AlphaVantage):
    def __init__(self, symbol):
        super().__init__()
        self.symbol = symbol
        self.url = f'{self.base_url}&function=TIME_SERIES_DAILY&symbol={self.symbol}&outputsize=compact'

    def get_data(self):
        self.r = requests.get(self.url)
        return self.r.json()

    def get_daily_data(self):
        data = self.get_data()
        return data['Time Series (Daily)']

def test():
    symbol = 'MSFT'
    a = daily(symbol)
    data = a.get_daily_data()
    print(data)

if __name__ == '__main__':
    test()