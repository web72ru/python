import requests
import lxml.html
from bs4 import BeautifulSoup
import csv
import re

CSV = 'loft4you.csv'

HOST = 'https://loft4you.ru/'
URL = 'https://loft4you.ru/catalog/disaynerskie_svetilniki'
HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36'
           }


def poluchaem_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

html = poluchaem_html(HOST)

print(html)