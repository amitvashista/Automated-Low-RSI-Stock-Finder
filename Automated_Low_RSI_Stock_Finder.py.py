#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt


def rsi(ticker,start,end,window_period,plot=False):
    data=yf.download(ticker,start,end)
    df=data['Adj Close'].diff(1)
    df.dropna(inplace=True)
    
    positive=df.copy()
    negative=df.copy()
    positive[positive<0]=0
    negative[negative>0]=0
    
    avg_gain=positive.rolling(window=window_period).mean()
    avg_loss=abs(negative.rolling(window=window_period).mean())
    relative_strength=avg_gain/avg_loss
    
    RSI=100.0-(100.0/(1.0+relative_strength))
    
    combine=pd.DataFrame()
    combine['Adj Close']=data['Adj Close']
    combine['RSI']=RSI
    
    if plot==True:
        plt.figure(figsize=(12,8))
        ax1=plt.subplot(211)
        ax1.plot(combine.index,combine['Adj Close'],color='lightgray')
        ax1.set_title('adjusted close price',color='white')
        ax1.grid(True,color='#555555')
        ax1.set_axisbelow(True)
        ax1.set_facecolor('black')
        ax1.figure.set_facecolor('#121212')
        ax1.tick_params(axis='x',colors='white')
        ax1.tick_params(axis='y',colors='white')

        ax2=plt.subplot(212,sharex=ax1)
        ax2.plot(combine.index,combine['RSI'],color='lightgray')
        ax2.axhline(0,linestyle='--',color='#ff0000')
        ax2.axhline(20,linestyle='--',color='#ffaa00')
        ax2.axhline(30,linestyle='--',color='#00ff00')
        ax2.axhline(50,linestyle='--',color='#cccccc')
        ax2.axhline(70,linestyle='--',color='#00ff00')
        ax2.axhline(80,linestyle='--',color='#ffaa00')
        ax2.axhline(100,linestyle='--',color='#ff0000')
        
        ax2.set_title('RSI value',color='white')
        ax2.grid(False)
        ax2.set_facecolor('black')
        ax2.figure.set_facecolor('#121212')
        ax2.tick_params(axis='x',colors='white')
        ax2.tick_params(axis='y',colors='white')
        plt.show()
    return combine


start=dt.datetime(2020,1,1)
end=dt.datetime.now()
ticker='RELIANCE.NS'


RSI=rsi(ticker,start,end,window_period=14,plot=True)


file=pd.read_csv(r'C:\Users\AMIT VASHISTHA\OneDrive\Desktop\TICKER NAME.csv')
print(file.shape)


list_of_share_with_low_rsi=[]
i=0
for ticker in file['Symbol.NS']:
    if i==1000:
        break
    start=dt.datetime(2022,1,1)
    end=dt.datetime.now()
    RSI=rsi(ticker,start,end,window_period=14)
    last_value=RSI['RSI'].iloc[-1]
    if last_value<20:
        list_of_share_with_low_rsi.append(ticker)
    i+=1
    print(i)


print(i)

print(list_of_share_with_low_rsi)


RSI


print(len(list_of_share_with_low_rsi))




