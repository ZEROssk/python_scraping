#coding:utf-8
import requests
import re
import os
import sys
from bs4 import BeautifulSoup

LIST_URI = "https://grand_order.wicurio.com/index.php?%E3%81%90%E3%81%A0%E3%81%90%E3%81%A0%E5%9C%9F%E4%BD%90%E5%90%8C%E7%9B%9F"

rows = BeautifulSoup(
    requests.get(LIST_URI).text,
    'lxml',
).find(
    'table',
    class_='style_table',
).find_all(
    'tr'
)

for row in rows:
    eachPageAtag = row.find('a')

    if eachPageAtag is None:
        continue

    idNo = row.find('td').text

    imgsrc = BeautifulSoup(
        requests.get(
            row.find('a').get('href')
        ).text,
        'lxml',
    ).find(
        'img',
        src = re.compile(
            r'^https://grand_order\.wicurio\.com/index\.php.+$'
        ),
    ).get('src')

    print(
        '{}: {}'.format(
            idNo,
            imgsrc,
        )
    )

