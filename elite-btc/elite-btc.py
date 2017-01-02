# coding=utf-8
from slackbot.bot import listen_to
import re
import json
import os


@listen_to('!price', re.IGNORECASE)
def btc_price(message):
    with open(os.path.abspath(os.path.join("btc_price_cache.txt"))) as data_file:
        data = json.load(data_file)

    price = data['data']['amount']
    price = price.encode("utf-8").strip()
    message.reply(('Current Price: %s%s' % ("£", price)))
