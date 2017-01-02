import urllib
import json

data = json.loads(urllib.urlopen("https://api.coinbase.com/v2/prices/BTC-GBP/buy").read())

with open('btc_price_cache.txt', 'w') as outfile:
    json.dump(data, outfile)
