import requests, lxml.html, re, datetime
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

session = requests.Session()

исходник = 'https://www.tyumen-city.ru/sobitii/'
шапка = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36'
}


def получаем_хтмл(ссылка):
    ответ = session.get(ссылка, headers=шапка, verify=False)
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
            '//div[@id="news"]//h4[contains(text(), " уче") and contains(text(), "анят") and contains(text(), "отмен")]/text()')
        дата = икспас.xpath('//*[@id="news"]/h4[1]/span/text()')
        дата = re.split(r'[\.\s\:]+', дата[0])
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

    return новости


def запись_новости(новости):
    with  open('последняя_новость.txt', 'r+') as дата_новости:
        if новости['дата'] > дата_новости.readline:
            дата_новости.write(новости['дата'])



print(выборка_новостей())
