import requests
# import lxml.html
# import time
# from selenium import webdriver
# from selenium.webdriver import FirefoxOptions

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
#
# browser = webdriver.Chrome(options=options)
#
# start_time = time.time()
# print("Первичный запрос")
# browser.get('https://petrovich.ru')
# print("Первичный выполнен")
# print("--- %s seconds ---" % (time.time() - start_time))
#
# следы = browser.get_cookies()

# url = 'https://petrovich.ru'
# r = requests.get(url, cookies=следы)
# print(r, r.text)
# print(r.cookies)

#
# след_строка = ''
# print(следы)
# exit()
# for ключ, значение in следы:
#     след_строка += str(ключ)+'='+str(следы[ключ])+'; '
# print(след_строка)
# exit()
#
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
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'cookie': 'SNK=116; u__typeDevice=desktop; u__geoUserChoose=1; SIK=dAAAAHXUgCIL46gSoEMKAA; SIV=1; C_mEdw5ztuoe2pf0oEopy6dlcVaqo=AAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D8AAGAhINTpQU5K30hhIfmb_xg-oLUUX3Y; _gcl_au=1.1.908313899.1670042088; tmr_lvid=a33634d191114965d76a871fc4ef16e6; tmr_lvidTS=1670042091534; _gid=GA1.2.75997037.1670042092; _ym_uid=1670042092119446854; _ym_d=1670042092; _ym_isad=1; UIN=dAAAAK7ZmBRIhTdwlEu9Cbuv4R9vDgVCEeOoEpxTCgA; ssaid=d5d727b0-72c3-11ed-af7f-7f9c58b2885d; rrpvid=554093126235759; rcuid=638ad1f27845cfff5fd2dcc8; aplaut_distinct_id=pveK66eGpCE8; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; dd_custom.lastViewedProductImages=[%2212716%22%2C%22%22%2C%22%22]; dd_custom.ts12={%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221670025600%22:12}}; dd_custom.lt11=2022-12-03T07:17:30.376Z; rrlevt=1670051855672; dd__persistedKeys=[%22custom.lastViewedProductImages%22%2C%22custom.lt13%22%2C%22custom.ts14%22%2C%22custom.ts12%22%2C%22custom.lt11%22]; dd_custom.lt13=2022-12-03T08:07:29.014Z; dd_custom.ts14={%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221670025600%22:56}}; digi_uc=W1sidiIsIjYxMTg0NCIsMTY3MDA1MTg1MjE4M10sWyJ2IiwiMTQwMjE3IiwxNjcwMDQ5NDk3NDQyXSxbInYiLCI4MTA0NTkiLDE2NzAwNDI0MDA5OTRdLFsiY3YiLCIxNDAyMTciLDE2NzAwNTQ1NTY1NjJdLFsiY3YiLCI2ODc1MzMiLDE2NzAwNTQ1MzcyNzZdLFsiY3YiLCI2MjMzNTMiLDE2NzAwNDk5Mjc4MTJdLFsiY3YiLCI2NTYxNzIiLDE2NzAwNDk4OTMwNDldLFsiY3YiLCI2MzQwMzkiLDE2NzAwNDk4NDA3NTNdLFsiY3YiLCI5MjY4NzgiLDE2NzAwNDk4MTE1NDldLFsiY3YiLCIxMDE4NDUiLDE2NzAwNDk3Mzc5NzddLFsiY3YiLCIxMjY5MTYiLDE2NzAwNDg3MTU0OTJdLFsiY3YiLCI2NzI1MzAiLDE2NzAwNDgwMzcwNTRdLFsiY3YiLCIxNTA5NjYiLDE2NzAwNDM5NDI1MzBdLFsiY3YiLCIxMDgyMDgiLDE2NzAwNTQ4NDI4MDVdXQ==; u__geoCityGuid=bd10887b-2da4-11df-942d-0023543d7b52; _ga=GA1.2.1071695914.1670042092; __tld__=null; dd__lastEventTimestamp=1670059396857; mindboxDeviceUUID=14c3907a-f9ad-49d9-9d07-6de00b365e20; directCrm-session=%7B%22deviceGuid%22%3A%2214c3907a-f9ad-49d9-9d07-6de00b365e20%22%7D; _ga_XW7S332S1N=GS1.1.1670059181.3.1.1670059603.60.0.0; qrator_msid=1670066563.151.TaCqUhCQudb7FOL9-nqdlqo0q8sgoudbnk153l2nsvv2ou9ke'
}

запрос_к_городам = 'https://api.petrovich.ru/geobase/v1.1/cities?city_code=spb&client_id=pet_site'
запрос_к_категориям = 'https://api.petrovich.ru/catalog/v2.3/sections/tree/3?city_code=rf&client_id=pet_site'


def получаем_хтмл(ссылка):
    хтмл = session.get(ссылка, headers=шапка)
    return хтмл


def получить_кода_городов(строка_запроса):
    получаем_хтмл('https://petrovich.ru')
    ответ_запроса = получаем_хтмл(строка_запроса)
    хтмл_текст = ответ_запроса.text
    print(хтмл_текст)


получить_кода_городов(запрос_к_городам)

# главные_категории = ['https://petrovich.ru/catalog/95761851/']
#
# for исходная_ссылка in исходные_ссылки:
#     страница = получаем_хтмл(исходная_ссылка)
#     икспас = lxml.html.document_fromstring(страница.text)
#     ссылки = икспас.xpath('//div[@class="sections-menu-content"]/div[@class="masonry"]/div[@class="masonry-brick"]/div[@class="subsection"]/a/@href')
#     for категория in ссылки:
#         категория = исходная_ссылка + категория
#         главные_категории.append(категория)
#         print(f'Собрано: {len(главные_категории)} ссылок на категории')
#
# print(главные_категории)

# def получаем_элемент_хтмл(ссылка):
#     ответ_запроса = session.get(ссылка, headers=шапка)
#     if ответ_запроса.status_code != 200:
#         print(f"Страница {ссылка} не загружена")
#         exit()
#     return lxml.html.document_fromstring(ответ_запроса.text)
#
#
# def собрать_коды_на_товары(ссылка_на_страницу):
#     элемент_хтмл = получаем_элемент_хтмл(ссылка_на_страницу)
#     список_кодов_товаров = элемент_хтмл.xpath(
#         "//div[@data-item-code]/@data-item-code")
#     return список_кодов_товаров
#
#
# print(собрать_коды_на_товары('https://rf.petrovich.ru/catalog/12101/'))

# def собрать_товары_со_одной_страницы(ссылка_на_страницу):
#     ссылки_на_товары = собрать_коды_на_товары(ссылка_на_страницу)
#
#     for ссылка_на_товар in ссылки_на_товары:
#         элемент_хтмл = получаем_элемент_хтмл(ссылка_на_товар)
#         список_кодов_товаров = элемент_хтмл.xpath(
#             "//div[@data-item-code]/@data-item-code")
#         exit()
#
#     print(ссылки_на_товары)
#
#
# собрать_товары_со_одной_страницы(пробные_страницы[0])
