# -*- coding: utf-8 -*-
"""
Zerodha kiteconnect automated authentication
"""

from kiteconnect import KiteConnect
import requests
import json
import os


cwd = os.chdir("D:\\algo")

def autologin():   
    token_path = "api_key.txt"
    key_secret = open(token_path,'r').read().split()
    kite = KiteConnect(api_key=key_secret[0])
    sess = requests.Session()

    res = sess.get(kite.login_url())
    new_url = res.url

    res2 = sess.post('https://kite.zerodha.com/api/login', data={'user_id': key_secret[2], 'password': key_secret[3]})
    res_json = json.loads(res2.text)

    res3 = sess.post('https://kite.zerodha.com/api/twofa', data={'user_id': res_json.get('data').get('user_id'),
                                                                 'request_id': res_json.get('data').get('request_id'),
                                                                 'twofa_value': key_secret[4]})
    
    res4 = sess.get(new_url+'&skip_session=true', allow_redirects=False)
    request_token_url = res4.headers['Location']

    request_token = request_token_url.split('=')[1].split('&action')[0]
    
    return request_token

request_token = autologin()


#generating and storing access token - valid till 6 am the next day
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
data = kite.generate_session(request_token, api_secret=key_secret[1])
with open('access_token.txt', 'w') as file:
        print(data['access_token'])
        file.write(data["access_token"])
