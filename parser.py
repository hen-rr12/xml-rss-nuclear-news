import requests
from lxml import etree
import urllib3

from RSS import RSS
from Article import Article

url = "https://www.world-nuclear-news.org/?rss=feed"
root = etree.parse(urllib3.request('GET', url))

channelPath = '//rss//channel'
articlePath = '//rss//channel//item'

def get_rss_channel_details(channel, channelPath):

    obs = channel.xpath(channelPath)
    rssChannel = RSS(obs[0].xpath('//title')[0].text,
                  obs[0].xpath('//link')[0].text,
                  obs[0].xpath('//description')[0].text,
                  obs[0].xpath('//language')[0].text)
    return rssChannel

def get_list_of_rss_articles(channel, articlePath):

    i = 0
    articleList = []
    for obs in channel.xpath(articlePath):
        article = Article(obs.xpath('//guid')[i].text,
                          obs.xpath('//title')[i].text,
                          obs.xpath('//description')[i].text,
                          obs.xpath('//pubDate')[i].text,
                          obs.xpath('//link')[i].text)
        i += 1
        articleList.append(article)

    return articleList

print(get_rss_channel_details(root, channelPath))

for i in range(0,len(get_list_of_rss_articles(root, articlePath))):
    print(get_list_of_rss_articles(root, articlePath)[i])