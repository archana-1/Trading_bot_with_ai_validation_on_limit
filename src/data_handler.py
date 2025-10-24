import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period='1d', interval='1m'):
    data = yf.download(ticker, period=period, interval=interval)
    return data


