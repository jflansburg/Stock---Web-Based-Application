import sys

from yahoo_fin import stock_info as si
from datetime import *
from win10toast import ToastNotifier 
import pandas as pd

file = pd.read_csv(r'C:\\Users\\jackf\\Desktop\\Python\\Test Data\\Watchlist.csv')
tickers = file.iloc[:,0]
price = file.iloc[:,1]
trigger = file.iloc[:,2]

#for loop to get live price
for ticker in tickers:
    if ticker == 'AAPL':
        apple = round(si.get_live_price(ticker),2)
    elif ticker == 'NVDA':
        nvidia = round(si.get_live_price(ticker),2)
    elif ticker == 'DFEN':
        dfen = round(si.get_live_price(ticker),2)



current_time = datetime.datetime.now().strftime('%I:%M:%S')
toast = ToastNotifier()
toast.show_toast("Stock Update Notification", f"As of {current_time} stock prices are as follows: \n AAPL ${apple} \n NVDA ${nvidia} \n DFEN ${dfen}", duration= 20)
