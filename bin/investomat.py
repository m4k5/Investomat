"""
Investomat by m4k5
24/7 personal automatic investor powered with Python
Currently supports:
- Bitcoin (exchanges listed in bitcoin.py)
- gold (logging gold possesions and checking their values from zlotagotowka.pl
"""
import os

import bitcoin
import configure
import gold

try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'investomat.conf')) as data:
        settings = data.read().splitlines()
        api_public = settings[0]
        api_secret = settings[1]
        address = settings[2]
        amount = settings[3]
        user = settings[4]
        password = settings[5]
        server = settings[6]
        port = settings[7]
        receipent = settings[8]
        gold_possesions = settings[9:]
except (IOError, IndexError, TypeError):
    configure.make_config('investomat.conf')
    exit()
bitbay = bitcoin.BitBayNet(api_public, api_secret)
exchange_price = bitcoin.crypto_price()
bitcoin_balance = bitcoin.get_address_balance(address)
buy_data = bitbay.buy_crypto(
    round(float(amount) / exchange_price, 8), exchange_price)
exchange_user_info = bitbay.get_balances()
print('BitBay:   {!s} PLN'.format(exchange_user_info['account_value']))
gold_value = gold.gold_value(gold_possesions)
print('Gold:     {!s} PLN'.format(gold_value))
