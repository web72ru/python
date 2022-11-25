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
    'http': 'http://62.113.109.137:80',
    'http': 'http://46.151.108.69:8081',
    'http': 'http://85.26.146.169:80',
    'http': 'http://185.221.160.176:80',
    'http': 'http://185.221.160.60:80',
    'http': 'http://91.142.149.51:80',
    'http': 'http://109.194.22.61:8080',
    'http': 'http://173.245.49.44:80',
    'http': 'http://173.245.49.38:80',
    'https': 'https://176.192.70.58:8007',
    'https': 'https://81.177.6.249:3128',
    'https': 'https://20.111.54.16:80',
    'https': 'https://185.73.203.66:3128',
    'https': 'https://117.251.103.186:8080',
    'https': 'https://89.43.31.134:3128',
    'https': 'https://169.57.1.85:8123',
    'https': 'https://176.192.70.58:8007',
    'https': 'https://193.37.214.45:42068',
    'https': 'https://20.111.54.16:80'
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
        h4 = икспас.xpath(
            '//div[@id="news"]//h4[contains(text(), "учеб") and contains(text(), "занят") and contains(text(), "отмен")]/text()')
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
