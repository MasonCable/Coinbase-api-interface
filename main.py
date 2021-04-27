import time, requests
from urls import *
from CoinAccount import Account
from auth_client import CBAuth
from MarketData import MarketData
from auth_credentials import PASSPHRASE, KEY, SECRET

auth = CBAuth(KEY, SECRET, PASSPHRASE)
accountData = Account()
marketData = MarketData()

print(marketData.product_trades("BTC"))
    

run = False
while run:
    for i in accountData.accounts():
        if i['available'] != '0':
            print(i)
    