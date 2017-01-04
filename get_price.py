# coding=utf-8
import os
import urllib
import json
import requests

from slackbot_settings import API_TOKEN


def get_cached_price():
    with open(os.path.abspath(os.path.join("btc_price_cache.txt"))) as data_file:
        data = json.load(data_file)

    return float(data['data']['amount'])


def get_new_price():
    data = json.loads(urllib.urlopen("https://api.coinbase.com/v2/prices/BTC-GBP/buy").read())

    with open('btc_price_cache.txt', 'w+') as outfile:
        json.dump(data, outfile)

    return float(data['data']['amount'])


def send_message(message):
    _vars = {
        'token': API_TOKEN,
        'channel': 'G3M1V6G2K',
        'text': message
    }
    url = 'https://slack.com/api/chat.postMessage?%s' % urllib.urlencode(_vars)
    requests.post(url)


def send_btc_update():
    old = get_cached_price()
    new = get_new_price()
    diff = (old - new) * -1
    percent = (diff / old * 100)
    percent_string = "{:.2f}".format(percent)

    info = "Was: £%s Now: £%s Diff: £%s (%s%s)" % (old, new, diff, percent_string, "%")

    if percent > 0:
        send_message("BTC is UP!")
        send_message("%s" % info)
    elif percent < 0:
        send_message("BTC is DOWN!")
        send_message("%s" % info)
    else:
        send_message("BTC is the same?")
        send_message("%s" % info)


send_btc_update()
