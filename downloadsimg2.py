#coding:utf-8
import requests
import re
import os
import sys
from bs4 import BeautifulSoup

iurl = input('URL>')
dirname = '/Users/zero/Desktop/' + input('file name ＞') + '/'

url = requests.get(iurl)
soup = BeautifulSoup(url.text,'lxml')
imgurl = soup.find_all('img',src=re.compile('http://'))

#URLの成形
#begin = 'http://'
#end = '.jpg'
os.mkdir(dirname)
#images = []
count = 0

#print(imgurl)

print('\n----------START----------\n')

#for imurl in imgurl:
#    r = re.compile( '(%s.*%s)' % (begin,end), flags=re.DOTALL )
#    m = r.search(imurl['src'])
#    imurl = ''

#    if m is not None:
#        imurl = m.group(0)

#    images.append(imurl)

#ファイル出力
for img in imgurl:
    count += 1
    re = requests.get(img['src'])
    print('Download:',img)

    with open(str(dirname)+str(count)+str('.jpg'),'wb') as file:
        file.write(re.content)

print('\n----------END----------\n')

