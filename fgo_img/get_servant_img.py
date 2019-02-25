#coding:utf-8
import requests
import re
import os
import sys
from bs4 import BeautifulSoup

imgURL = []

inputURL = 'https://grand_order.wicurio.com/index.php?%E3%82%B5%E3%83%BC%E3%83%B4%E3%82%A1%E3%83%B3%E3%83%88%E4%B8%80%E8%A6%A7'
dirname = '/home/zero/bot/fgo/fgo_servant'

os.mkdir(dirname)

bsURL = BeautifulSoup(
    requests.get(inputURL).text,
    'lxml',
).find(
    'table',
    class_='style_table',
).find_all(
    'tr'
)

for urllist in bsURL:
    fAtag = urllist.find('a')

    if fAtag is None:
        continue

    name = urllist.find('a').text
    rank = urllist.find('td').text
    no = urllist.find('th').text

    if name == '?':
        continue

    print("{}: {}".format(no, name))
    print("    - {}".format(urllist.find('a').get('href')))
    iURL = BeautifulSoup(
        requests.get(
            urllist.find('a').get('href')
        ).text,
        'lxml',
    ).find(
        'img',
        src = re.compile(
            'https://grand_order'
        ),
    ).get('src')

    print("    - {}".format(iURL))

    getimg = requests.get(iURL)

    filePath = '{}/No{} Rank{} {}.jpg'.format(
        dirname,
        no,
        rank,
        name.replace('/','／'),
    )

    with open(filePath, 'wb') as file:
        file.write(getimg.content)

