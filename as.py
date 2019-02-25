# coding: UTF-8

import requests
import re
from bs4 import BeautifulSoup

print('test')

get_amazon_url = input('URL >')

amazon_url = BeautifulSoup(requests.get(get_amazon_url).txt,'lxml').find('span',style=re.compile('priceblock_ourprice')).txt

print('値段:',amazon_url)

