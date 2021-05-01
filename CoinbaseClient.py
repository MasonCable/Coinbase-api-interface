import requests, hmac, hashlib, time, base64
from requests.auth import AuthBasea
from urls import *
from auth_credentials import KEY, SECRET, PASSPHRASE

class Client:
    def __init(self):
        self.auth = CBAuth(KEY, SECRET, PASSPHRASE)
    
    def accounts(self):
        response = requests.get(account_url(), auth=self.auth).json()

        return response
    
    def orders(self):
        response = requests.get(get_orders(), auth=self.auth).json()

        return response
    
    def transfers(self):
        response = requests.get(get_transfers(), auth=self.auth).json()

        return response
    
        def currencies(self):
        response = requests.get(get_currencies()).json()

        return response

    def products(self):
        response = requests.get(get_products()).json()

        return response
    

    def product_from_id(self, product_id):
        response = requests.get(get_product_by_id(product_id)).json()

        return response
    
    def product_order_book(self, product_id, level):
        response = requests.get(get_product_order_book(product_id, level)).json()

        return response

    def product_trades(self, product_id):
        response = requests.get(get_product_trades(product_id)).json()

        return response
    
    def get_historic_rates(self, product_id, start, end, timeslice):
        url = get_historic_trades(product_id, start, end, timeslice)
        response = requests.get(url).json()

        return response

    def get_24hr_stats(self, product_id):
        response = requests.get(get_24hr_stats(product_id)).json()

        return response



def get_auth_headers(timestamp, message, api_key, secret_key, passphrase):
    message = message.encode('ascii')
    hmac_key = base64.b64decode(secret_key)
    signature = hmac.new(hmac_key, message, hashlib.sha256)
    signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')
    return {
        'Content-Type': 'Application/JSON',
        'CB-ACCESS-SIGN': signature_b64,
        'CB-ACCESS-TIMESTAMP': timestamp,
        'CB-ACCESS-KEY': api_key,
        'CB-ACCESS-PASSPHRASE': passphrase
    }

class CBAuth(AuthBase):
    # Provided by CBPro: https://docs.pro.coinbase.com/#signing-a-message
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = ''.join([timestamp, request.method,
                           request.path_url, (request.body or '')])
        request.headers.update(get_auth_headers(timestamp, message,
                                                self.api_key,
                                                self.secret_key,
                                                self.passphrase))
        return request