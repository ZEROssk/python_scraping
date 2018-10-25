#coding:utf-8
import requests
import re
import os
import sys
from bs4 import BeautifulSoup

imgURL = []

inputURL = input('URL>')
dirname = '/Users/zero/Desktop/' + input('file name ＞')

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
    no = urllist.find('td').text

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

    filePath = '{}/{}.jpg'.format(
        dirname,
        name.replace('/','／'),
    )

    with open(filePath, 'wb') as file:
        file.write(getimg.content)

