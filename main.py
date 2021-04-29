import time, requests
from urls import *
from CoinAccount import Account
from auth_client import CBAuth
from MarketData import MarketData
from auth_credentials import PASSPHRASE, KEY, SECRET

auth = CBAuth(KEY, SECRET, PASSPHRASE)
accountData = Account()
marketData = MarketData()

for i in accountData.accounts():
    if float(i['available']) != 0.00000000:
        print(i)
        
    

run = False
while run:
    for i in accountData.accounts():
        if i['available'] != '0':
            print(i)
    