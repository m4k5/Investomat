"""
Investomat by m4k5
24/7 personal automatic investor powered with Python
Currently supports:
- Bitcoin (exchanges listed in bitcoin.py)
"""
try:
    import hashlib
    import hmac
    import requests
    import time
    import datetime
except ImportError:
    print 'Missing dependencies, please check requirments.'
    exit()
import notify
import bitcoin
try:
    with open('data') as data:
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
except (IOError, IndexError, TypeError):
    print 'CONFIGURE.PY'
    exit()
exchange = bitcoin.BitBay_net(api_public, api_secret)
exchange_balances = exchange.getBalance()
exchange_price = exchange.btcPrice()
bitcoin_balance = bitcoin.getAddressBalance(address)
result = ''
for i in exchange_balances:
    if (exchange_balances[i]['available'] != '0' or
            exchange_balances[i]['locked'] != '0'):
        if i != 'PLN':
            result += 'Available for {}: {} {}\n'.format(
                i, exchange_balances[i]['available'], i)
            result += 'Locked for {}: {} {}\n\n'.format(
                i, exchange_balances[i]['locked'], i)
        else:
            result += 'Available for {}: {} {}\n'.format(
                i, round(float(exchange_balances[i]['available']), 2), i)
            result += 'Locked for {}: {} {}\n\n'.format(
                i, round(float(exchange_balances[i]['locked']), 2), i)
result += 'Address balance is {!s} BTC (~{!s} PLN)\n\n'.format(
    bitcoin_balance, round(bitcoin_balance * exchange_price, 2))
buy_data = exchange.buyCrypto(
    round(float(amount) / exchange_price, 8), exchange_price)
result += 'Bought {:.8f} BTC @ {} for {!s} PLN'.format(
    buy_data['amount'], buy_data['rate'], round(float(buy_data['price'])), 2)
print result
notify.send_email('Report Investomat', receipent, result, user, password,
                  server, port)
