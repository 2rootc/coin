import pandas as pd
import pyupbit
import ssl


tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)