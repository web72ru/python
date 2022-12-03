import requests, lxml.html
from al_re import reg

session = requests.Session()
исходные_ссылки = ['https://petrovich.ru', 'https://moscow.petrovich.ru', 'https://arkhangelsk.petrovich.ru',
                   'https://astrakhan.petrovich.ru', 'https://novgorod.petrovich.ru',
                   'https://vladimir.petrovich.ru', 'https://volzhskiy.petrovich.ru', 'https://vyborg.petrovich.ru',
                   'https://gatchina.petrovich.ru', 'https://gubkin.petrovich.ru',
                   'https://zheleznogorsk.petrovich.ru', 'https://i-ola.petrovich.ru', 'https://kazan.petrovich.ru',
                   'https://kaluga.petrovich.ru', 'https://kingisepp.petrovich.ru', 'https://kirov.petrovich.ru',
                   'https://kursk.petrovich.ru', 'https://lipetsk.petrovich.ru', 'https://luga.petrovich.ru',
                   'https://magnitogorsk.petrovich.ru', 'https://naberezhnye-chelny.petrovich.ru',
                   'https://nizhnevartovsk.petrovich.ru', 'https://nizhniy-novgorod.petrovich.ru',
                   'https://nizhniy-tagil.petrovich.ru', 'https://orel.petrovich.ru',
                   'https://pervouralsk.petrovich.ru', 'https://petrozavodsk.petrovich.ru',
                   'https://pskov.petrovich.ru', 'https://ryazan.petrovich.ru', 'https://stary-oskol.petrovich.ru',
                   'https://syktyvkar.petrovich.ru', 'https://tver.petrovich.ru', 'https://tobolsk.petrovich.ru',
                   'https://tula.petrovich.ru', 'https://cheboksary.petrovich.ru', 'https://engels.petrovich.ru']
шапка = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2500 Yowser/2.5 Safari/537.36'
}


def получаем_хтмл(ссылка):
    хтмл = session.get(ссылка, headers=шапка)
    return хтмл


главные_категории = ['https://petrovich.ru/catalog/8738/']
'''
for исходная_ссылка in исходные_ссылки:
    страница = получаем_хтмл(исходная_ссылка)
    икспас = lxml.html.document_fromstring(страница.text)
    ссылки = икспас.xpath('//div[@class="sections-menu-content"]/div[@class="masonry"]/div[@class="masonry-brick"]/div[@class="subsection"]/a/@href')
    for категория in ссылки:
        категория = исходная_ссылка + категория
        главные_категории.append(категория)
        print(f'Собрано: {len(главные_категории)} ссылок на категории')
'''

главные_категории_с_пагинацией = []
for главная_ссылка in главные_категории:
    страница = получаем_хтмл(главная_ссылка)
    икспас = lxml.html.document_fromstring(страница.text)
    строка_найдено_товаров = икспас.xpath('//p[@data-test="products-counter"]')
    #поиск_количества = 'data-test="products-counter".*?>Найдено товаров:\s.*?(\d+)<'
    #товаров_на_странице = reg(страница, поиск_количества, 'ms')
    print(строка_найдено_товаров)
#    пагинация = товаров_на_странице // 20
#    for ч in range(0, пагинация):
#        главная_с_пагинацией = главная_ссылка + '?p=' + ч
#        главные_категории_с_пагинацией.append(главная_с_пагинацией)


