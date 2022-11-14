import requests
import lxml.html
from bs4 import BeautifulSoup
import csv
import re

HOST = 'https://loft4you.ru/'
URL = 'https://loft4you.ru/catalog/disaynerskie_svetilniki'
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


ssylki_na_tovary = sbor_ssylok_so_vseh_stranic()


def dannye_tovara():
    i = 0
    katalog = []
    for url_1_tovara in ssylki_na_tovary:
        html_tovara = poluchaem_html(url_1_tovara)
        tree = lxml.html.document_fromstring(html_tovara.text)
        html_text = html_tovara.text

        artikul = tree.xpath('//span[@itemprop="sku"]/text()')
        h1 = tree.xpath('//h1/text()')
        cena = tree.xpath('//span[@itemprop="price"]/text()')
        cena = re.sub(r'\s+', '', cena[0])
        izy = tree.xpath('//a[@class="fancybox"]/@href')
        harakteristiki = re.findall(r'<ul.*?id=\"product_options\">.*?</ul>', html_text, flags=re.MULTILINE)

        katalog.append({
            'артикул': artikul,
            'название': h1,
            'категория': ['Дизайнерские светильники'],
            'цена': cena,
            'изы': izy,
            'характеристики': harakteristiki
        })
        i += 1
        if i == 5:
            break
    return katalog


dannye = dannye_tovara()

print(dannye)
