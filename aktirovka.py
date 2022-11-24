import requests, lxml.html, re
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

session = requests.Session()

исходник = 'https://www.tyumen-city.ru/'
шапка = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36'
}


def получаем_хтмл(ссылка, params=''):
    ответ = requests.get(ссылка, headers=шапка, params=params, verify=False)
    хтмл_страницы = ответ.content.decode('windows-1251')

    return хтмл_страницы


хтмл_страницы = получаем_хтмл(исходник)


def находим_новость(хтмл_страницы):
    икспас = lxml.html.document_fromstring(хтмл_страницы.text)
    ссылки_на_новость = икспас.xpath('//a[@class="testt"]/@href')

    return ссылки_на_новость


#ссылки_на_новость = находим_новость(хтмл_страницы)

print(хтмл_страницы)
