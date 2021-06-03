import requests
from lxml import etree
import urllib

url = "https://www.world-nuclear-news.org/?rss=feed"
root = etree.parse(urllib.request.urlopen(url))

for obs in root.xpath('rss//channel//title'):
    print(obs)
    price = obs.xpath('./base:OBS_VALUE').text
    print(price)