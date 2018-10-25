#coding:utf-8
#LINEスタンプ取得用
import requests
import re
import os
import sys
from bs4 import BeautifulSoup

#URL指定
iurl = input('URL >')
#file名指定
dirname = '/Users/zero/Desktop/' + input('file name >') + '/'

#指定したLINEスタンプストアから画像URLを取得
url = requests.get(iurl)
soup = BeautifulSoup(url.text,'lxml')
imgs = soup.find_all('span',style=re.compile('https://stickershop.line-scdn.net/stickershop/v1/sticker'))

#画像URLの成形
begin = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'
end = '/ANDROID/sticker.png'
os.mkdir(dirname)
images = []
count = 0

print('\n-----START-----\n')

for ur in imgs:
    r = re.compile( '(%s.*%s)' % (begin,end), flags=re.DOTALL)
    m = r.search(ur['style'])
    ur = ''

    if m is not None:
        ur = m.group(0)

    images.append(ur)

#ファイルへの書き込み
for imgurl in images:
    count += 1
    re = requests.get(imgurl)
    print('Download:',imgurl)

    with open(str(dirname)+str(count)+str('.png'),'wb') as file:
        file.write(re.content)

print('\n-----END-----\n')

