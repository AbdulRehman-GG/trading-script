import alpaca_trade_api as tradeapi

# Alpaca API credentials Here!
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'
BASE_URL = 'https://paper-api.alpaca.markets'

# Connect to the Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL, api_version='v2')

# Your Trading Strategy

# Define a function to execute your strategy
def execute_strategy():
    # Get account information
    account = api.get_account()

    # Check if the market is open
    clock = api.get_clock()
    if not clock.is_open:
        print("Market is closed")
        return

    # Get the latest price data for your target stock
    symbol = 'AAPL' # Replace with your target stock symbol
    barset = api.get_barset(symbol, 'minute', limit=1)
    bars = barset[symbol]

    # Execute your trading strategy based on the latest price data


# Run the script continuously
while True:
    execute_strategy()
