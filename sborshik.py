# проверка
import requests
import lxml
from bs4 import BeautifulSoup
import csv

HOST = 'https://loft4you.ru/'
URL = 'https://loft4you.ru/catalog/disaynerskie_svetilniki'
tovar = 'https://loft4you.ru/catalog/like_modo'
HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36'
           }

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_ssylki(html):
    tree = lxml.html.document_fromstring(html.text)
    a_spis = tree.xpath("//div[@class='item_link']/a/@href")
    return a_spis

def sbor_ssylok_so_vseh_stranic():
    vse_ssylki = []
    for i in range(1, 1):
        print(f'Обрабатывается страница {i}')
        ssylka = URL + "/" + str(i)
        html = get_html(ssylka)
        ssylki_na_tovary = get_ssylki(html)
        vse_ssylki.extend(ssylki_na_tovary)
    vse_ssylki = list(set(vse_ssylki))
    print(len(vse_ssylki))

def sbor_dannyh_tovara():
    tree = lxml.html.document_fromstring(html.text)
    dannye_tovara = []
    dannye_tovara.append(
        {
            'артикул': tree.xpath("//span[@itemprop='sku']"),
            'название': tree.xpath("//h1"),
            'категория': tree.xpath("//div[@id='breadcrumps']/a/span"),
            'цена': tree.xpath("//span[@class='item_cost']/text()"),
            'описание': tree.xpath("//div[@id='description_box']/div[1]")
        }
    )
    print(dannye_tovara)


html = get_html(URL)
#ssylki = get_ssylki(html)
ssylki = sbor_ssylok_so_vseh_stranic()

#print(ssylki)

