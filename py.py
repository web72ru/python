import requests as r
import lxml.html

шапка = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36'
}

otvet = r.get('https://www.tyumen-city.ru/sobitii/', headers=шапка, verify=False)


soobchenie = []
if otvet.status_code == 200:
    html_text = otvet.content.decode('windows-1251')
    derevo = lxml.html.document_fromstring(html_text)
    hrefki = derevo.xpath("//div[@id='news']//a[text() = 'подробно']/@href")
    if hrefki:
        hrefki = reversed(hrefki)
        for href in hrefki:
            if href:
                otvet = r.get(href, headers=шапка, verify=False)
                html_text = otvet.content.decode('windows-1251')
                derevo = lxml.html.document_fromstring(html_text)
                h4_el = derevo.xpath("//div[@id='news']//h4[contains(text(), 'отменяются') and contains(text(), 'занятия')]/text()")
                if h4_el:
                    soobchenie.append(h4_el[0].strip())
                if len(soobchenie) == 2:
                    break
print(soobchenie)