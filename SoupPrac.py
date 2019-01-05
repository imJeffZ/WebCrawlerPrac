#! /usr/bin/python
# coding: UTF-8
import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent': 'JeffBot'}
r = requests.get(link, headers= headers)
soup = BeautifulSoup(r.text, "lxml")
title = soup.find("h1", class_ = "post-title").a.text.strip()
print(title)
import codecs
with codecs.open('title.txt', 'a+', 'utf-8') as f:
    f.write(title)
