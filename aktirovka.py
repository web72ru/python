import requests, lxml.html, re, time, random
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

session = requests.Session()

исходник = 'https://www.tyumen-city.ru/sobitii/'
шапка = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36'
}

proxies = {
    'http': 'http://203.23.103.60:80',
    'https': 'https://176.192.70.58:8007'
}


def получаем_хтмл(ссылка, params=''):
    ответ = requests.get(ссылка, headers=шапка, params=params, proxies=proxies, verify=False)
    хтмл = ответ.content.decode('windows-1251')

    return хтмл


хтмл_страницы = получаем_хтмл(исходник)


def находим_ссылки(страница):
    икспас = lxml.html.document_fromstring(страница)
    ссылки = икспас.xpath('//a[@class="testt"]/@href')

    return ссылки


ссылки_на_новость = находим_ссылки(хтмл_страницы)
ссылки_на_новость = ссылки_на_новость[::-1]


def выборка_новостей():
    новости = []
    for ссылка in ссылки_на_новость:
        страница_новости = получаем_хтмл(ссылка)
        икспас = lxml.html.document_fromstring(страница_новости)
        h4 = икспас.xpath('//div[@id="news"]//h4[contains(text(), "учеб") and contains(text(), "занят") and contains(text(), "отмен")]/text()')
        дата = икспас.xpath('//*[@id="news"]/h4[1]/span/text()')
        описание = икспас.xpath('//*[@id="news"]/div[1]/div/*/text()')
        иза = икспас.xpath('//*[@id="news"]/div[1]/img/@src')
        if h4:
            новости.append({
                'дата': дата,
                'заголовок': h4,
                'описание': описание,
                'иза': иза,
                'ссылка': ссылка
            })
        time.sleep(random.randint(10, 20))
    return новости


print(выборка_новостей())
