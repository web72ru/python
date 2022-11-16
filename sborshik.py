import requests
import lxml.html
from bs4 import BeautifulSoup
import csv
import re

# CSV = loft4you.csv

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
    kluchi = ['артикул', 'название', 'категория', 'цена', 'изы']
    for url_1_tovara in ssylki_na_tovary:
        html_tovara = poluchaem_html(url_1_tovara)
        tree = lxml.html.document_fromstring(html_tovara.text)

        artikul = tree.xpath('//span[@itemprop="sku"]/text()')
        h1 = tree.xpath('//h1/text()')
        cena = tree.xpath('//span[@itemprop="price"]/text()')
        cena = re.sub(r'\s+', '', cena[0])
        izy = tree.xpath('//a[@class="fancybox"]/@href')
        li_spisok = tree.xpath('//ul[@id="product_options"]/li')
        harakteristiki = []

        for li in li_spisok:
            kluch = li.xpath("strong/text()")[0]
            znach = li.xpath("strong[contains(text(),'" + kluch + "')]/ancestor::li/text()")
            harakteristiki.append([kluch, znach])
            kluchi.append(kluch)

        katalog.append({
            kluchi[0]: artikul,
            kluchi[1]: h1,
            kluchi[2]: ['Дизайнерские светильники'],
            kluchi[3]: cena,
            kluchi[4]: izy
        })
        for kluch_znach in harakteristiki:
            katalog[-1].update({kluch_znach[0]: kluch_znach[1]})

        i += 1
        if i == 5:
            break
    return katalog, kluchi


dannye = dannye_tovara()[0]
kluchi_povtory = dannye_tovara()[1]

kluchi = []
for kluch in kluchi_povtory:
    if kluch not in kluchi:
        kluchi.append(kluch)

'''
def zapis(tovary, put):
    with open(put, 'w', newline='') as file:
        zapisy = csv.writer(file, delimiter=';')
        zapisy.writerow(set(kluchi))
'''

print(kluchi_povtory)
print(kluchi)

# print(dannye)
