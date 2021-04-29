import time, requests
from CoinAccount import Account
import argparse
from auth_client import CBAuth
from MarketData import MarketData
from auth_credentials import PASSPHRASE, KEY, SECRET
# Store user arguments as globals
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--buy", help="Buy $ASSET")
parser.add_argument("-p", "--price", help="What Price Would you like to buy/sell this asset at?")
parser.add_argument("-s", "--sell", help="Sell $ASSET")
parser.add_argument("-ep", "--executionprice", help="What price would you like this order to be executed at?")
args = parser.parse_args()
inputAsset = args.buy if args.buy else args.sell
inputBuyOrSell = 'buy' if args.buy else 'sell'
buyOrSellPrice = args.price
executionPrice = args.executionprice


def limit_buy(asset, price, executionPrice):
    market = MarketData()
    account = Account()
    response = market.product_from_id(asset)
    confirmTransaction = input('You would like to {0} ${1} worth of {2} when {2} reaches a price of ${3}\n (yes) Or (no)\n'.format(inputBuyOrSell, buyOrSellPrice ,inputAsset, executionPrice))
    if confirmTransaction:
        account.orders()
    else:
        return "Order Canceled, click up arrow to try again"


print(limit_buy(inputAsset, buyOrSellPrice, executionPrice))
    



    