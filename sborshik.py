import requests
import lxml.html
from bs4 import BeautifulSoup
import csv

HOST = 'https://loft4you.ru/'
URL = 'https://loft4you.ru/catalog/disaynerskie_svetilniki'
tovar = 'https://loft4you.ru/catalog/like_modo'
HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36'
           }

def poluchaem_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def poluchaem_ssylki(html):
    tree = lxml.html.document_fromstring(html.text)
    a_spis = tree.xpath("//div[@class='item_link']/a/@href")
    return a_spis

def sbor_ssylok_so_vseh_stranic():
    vse_ssylki = []
    for i in range(1, 2):
        print(f'Обрабатывается страница {i}')
        ssylka = URL + "/" + str(i)
        html = poluchaem_html(ssylka)
        ssylki_na_tovary = poluchaem_ssylki(html)
        vse_ssylki.extend(ssylki_na_tovary)
    vse_ssylki = list(set(vse_ssylki))
    return vse_ssylki

def sbor_dannyh_tovara(ssylki, params=''):
    tree = lxml.html.document_fromstring(html.text)
    r = requests.get('https://loft4you.ru/catalog/hico_round_corner_design', headers=HEADERS, params=params)
    print(r.text)

html = poluchaem_html(URL)
ssylki = sbor_ssylok_so_vseh_stranic()
tovary = poluchaem_ssylki(html)
sbor_dannyh = sbor_dannyh_tovara(ssylki)

print(sbor_dannyh)

