import requests
import time
import hmac
import hashlib
import json


class Check:
    def __init__(self):
        self.api_key = {
            'key': 'Your_API_Key',
            'secret': 'Your_Secrete_Key'
        }
        self.nonce = str(int(round(time.time() * 1000)))
        self.customer_id = '2859'

    def get_ticker(self):
        ticker = requests.get('https://kiwi-coin.com/api/ticker/')
        return json.loads(ticker.text)

    def get_orderbook(self):
        orderbook = requests.get('https://kiwi-coin.com/api/order_book/')
        return json.loads(orderbook.text)

    def get_balance(self):
        message = self.nonce + self.customer_id + self.api_key['key'] + ";balance"
        signature = hmac.new(str.encode(self.api_key['secret']), msg=str.encode(message),
                             digestmod=hashlib.sha256).hexdigest().upper()
        token = {
            'key': self.api_key['key'],
            'signature': signature,
            'nonce': self.nonce
        }
        balance = requests.post('https://kiwi-coin.com/api/balance/', token)
        return json.loads(balance.text)

    def get_open_orders(self):
        message = self.nonce + self.customer_id + self.api_key['key'] + ";open_orders"
        signature = hmac.new(str.encode(self.api_key['secret']), msg=str.encode(message),
                             digestmod=hashlib.sha256).hexdigest().upper()
        token = {
            'key': self.api_key['key'],
            'signature': signature,
            'nonce': self.nonce
        }
        openorders = requests.post('https://kiwi-coin.com/api/open_orders/', token)
        return json.loads(openorders.text)


class Trade:
    def __init__(self):
        self.api_key = {
            'key': 'Your_API_Key',
            'secret': 'Your_Secrete_Key'
        }
        self.nonce = str(int(round(time.time() * 1000)))
        self.customer_id = '2859'

    def cancel_order(self, orderid):
        self.orderid = str(orderid)
        message = self.nonce + self.customer_id + self.api_key['key'] + ";cancel_order," + self.orderid
        signature = hmac.new(str.encode(self.api_key['secret']), msg=str.encode(message),
                             digestmod=hashlib.sha256).hexdigest().upper()
        token = {
            'key': self.api_key['key'],
            'signature': signature,
            'nonce': self.nonce,
            'id': self.orderid
        }
        cancel_trade = requests.post('https://kiwi-coin.com/api/cancel_order/', token)
        return cancel_trade

    def buy_limit_order(self, price, amount):
        self.price = str(price)
        self.amount = str(amount)
        message = self.nonce + self.customer_id + self.api_key['key'] + ";sell," + self.price + "," + self.amount
        signature = hmac.new(str.encode(self.api_key['secret']), msg=str.encode(message),
                             digestmod=hashlib.sha256).hexdigest().upper()
        token = {
            'key': self.api_key['key'],
            'signature': signature,
            'nonce': self.nonce,
            'price': self.price,
            'amount': self.amount
        }
        buy_limit_order = requests.post('https://kiwi-coin.com/api/buy/', token)
        print('buy order status is ')
        print(buy_limit_order)
        return buy_limit_order

    def sell_limit_order(self, price, amount):
        self.price = str(price)
        self.amount = str(amount)
        message = self.nonce + self.customer_id + self.api_key['key'] + ";sell," + self.price + "," + self.amount
        signature = hmac.new(str.encode(self.api_key['secret']), msg=str.encode(message),
                             digestmod=hashlib.sha256).hexdigest().upper()
        token = {
            'key': self.api_key['key'],
            'signature': signature,
            'nonce': self.nonce,
            'price': self.price,
            'amount': self.amount
        }
        sell_limit_order = requests.post('https://kiwi-coin.com/api/sell/', token)
        print('sell order status is ')
        print(sell_limit_order)
        return sell_limit_order