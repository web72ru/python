import requests, lxml.html, re, time, random
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

session = requests.Session()

исходник = 'https://www.tyumen-city.ru/sobitii/'
шапка = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36'
}


def получаем_хтмл(ссылка, params=''):
    ответ = requests.get(ссылка, headers=шапка, params=params, verify=False)
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
        дата = икспас.xpath('//h4[@class="first"]')
        if h4:
        	предметы = {
        		'дата': дата
        		'заголовок':
        		'описание':
        		'иза':
        		'ссылка': ссылка
        	}
       
        print(h4)
        #break
        time.sleep(random.randint(10, 20))

   


выборка_новостей()
