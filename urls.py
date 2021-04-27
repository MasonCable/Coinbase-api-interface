# All of the urls that we are going to need

def account_url():
    return 'https://api.pro.coinbase.com/accounts'

def account_from_id_url(account_id):
    return 'https://api.pro.coinbase.com/accounts/{0}'.format(account_id)

# Post to this url to place order
def place_order():
    """
        {
            "size": "0.01",
            "price": "0.100",
            "side": "buy",
            "product_id": "BTC-USD"
        }
    """
    return 'https://api.pro.coinbase.com/orders'

def cancel_order(order_id):
    # Take the ID from the order above and post here
    return 'https://api.pro.coinbase.com/orders/{}'.format(order_id)

# This function will return all fo the orders
def get_orders():
    return 'https://api.pro.coinbase.com/orders'

def get_transfers():
    return 'https://api.pro.coinbase.com/transfers'

def get_currencies():
    return 'https://api.pro.coinbase.com/currencies'

def get_currency_from_id(product_id):
    return 'https://api.pro.coinbase.com/currencies/{0}'.format(product_id)

def get_products():
    return 'https://api.pro.coinbase.com/products'

def get_product_by_id(product_id):
    return 'https://api.pro.coinbase.com/products/{0}'.format(product_id)

# Leve is an int value between 1 and 3
def get_product_order_book(product_id, level):
    if level:
        trueLevel = level
    else :
        trueLevel = 1
    return 'https://api.pro.coinbase.com/products/{0}/book?level={1}'.format(product_id, trueLevel)

def get_product_trades(product_id):
    return 'https://api.pro.coinbase.com/products/{0}/trades'.format(product_id)


def get_historic_trades(product_id, start, end, timeslice):
    return 'https://api.pro.coinbase.com/products/{0}/candles?start={1}&end={2}&grandularity={3}'.format(product_id, start, end, timeslice)

def get_24hr_stats(product_id):
    return 'https://api.pro.coinbase.com/products/{0}/stats'.format(product_id)

    