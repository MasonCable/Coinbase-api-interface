import time, requests
from urls import *
from auth_client import CBAuth
from auth_credentials import PASSPHRASE, KEY, SECRET

class Account:
    def __init__(self):
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