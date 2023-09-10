# useful website for learning this library: https://analyzingalpha.com/yfinance-python
import yfinance as yf #pip install yfinance

def get_tesla_stock_price_5_years():
    tesla = yf.Ticker("TSLA")
    stock_price = tesla.history(period = "5y", interval = "3mo")
    return stock_price

tesla_stock_price = get_tesla_stock_price_5_years()
print(tesla_stock_price)