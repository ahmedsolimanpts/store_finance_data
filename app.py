import pandas as pd 
# import yfinance as yf
from yahoo_fin.stock_info import get_data
import time
import datetime as dt


if __name__ == '__main__':
    df = get_data('aapl',
    start_date='2000-1-1',
    end_date=time.ctime())
    file_name = './Data/'+str(dt.datetime.today().day) + '_'+ str(dt.datetime.today().month) +'_'+ str(dt.datetime.today().year) +'.csv'
    df.to_csv(file_name)
    print('Done For Day : ' , dt.datetime.now())



