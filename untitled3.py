# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:55:00 2021

@author: mradu
"""
from kiteconnect import KiteConnect
import logging
import os

cwd = os.chdir("D:\\algo")

#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)


def placeMarketOrder(symbol,buy_sell,quantity):    
    # Place an intraday market order on NSE
    if buy_sell == "buy":
        t_type=kite.TRANSACTION_TYPE_BUY
    elif buy_sell == "sell":
        t_type=kite.TRANSACTION_TYPE_SELL
    kite.place_order(tradingsymbol=symbol,
                    exchange=kite.EXCHANGE_NSE,
                    transaction_type=t_type,
                    quantity=quantity,
                    order_type=kite.ORDER_TYPE_MARKET,
                    product=kite.PRODUCT_MIS,
                    variety=kite.VARIETY_REGULAR)




from flask import *
app= Flask(__name__)

@app.route('/tradingview',methods=['GET','POST'])
def home():
    json_data=request.json
    symbol=str(json_data["symbol"])
    SIGNAL=str(json_data["signal"])
    quantity=str(json_data["quantity"])
    print("WHAT TO DO--",SIGNAL,quantity,symbol)    
    return placeMarketOrder(symbol,SIGNAL,quantity)

if __name__ == "__main__":
    app.run(debug=False)
    

    
    
