import csv
import json
import os
import time

from multiprocessing.pool import ThreadPool as Pool
from os import listdir
from os.path import isfile, join

import requests

session = requests.Session()

следы = 'SNK=116; u__typeDevice=desktop; u__geoUserChoose=1; SIK=dAAAAHXUgCIL46gSoEMKAA; SIV=1; C_mEdw5ztuoe2pf0oEopy6dlcVaqo=AAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D8AAGAhINTpQU5K30hhIfmb_xg-oLUUX3Y; _gcl_au=1.1.908313899.1670042088; tmr_lvid=a33634d191114965d76a871fc4ef16e6; tmr_lvidTS=1670042091534; _gid=GA1.2.75997037.1670042092; _ym_uid=1670042092119446854; _ym_d=1670042092; _ym_isad=1; UIN=dAAAAK7ZmBRIhTdwlEu9Cbuv4R9vDgVCEeOoEpxTCgA; ssaid=d5d727b0-72c3-11ed-af7f-7f9c58b2885d; rrpvid=554093126235759; rcuid=638ad1f27845cfff5fd2dcc8; aplaut_distinct_id=pveK66eGpCE8; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; dd_custom.lastViewedProductImages=[%2212716%22%2C%22%22%2C%22%22]; dd_custom.ts12={%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221670025600%22:12}}; dd_custom.lt11=2022-12-03T07:17:30.376Z; rrlevt=1670051855672; dd__persistedKeys=[%22custom.lastViewedProductImages%22%2C%22custom.lt13%22%2C%22custom.ts14%22%2C%22custom.ts12%22%2C%22custom.lt11%22]; dd_custom.lt13=2022-12-03T08:07:29.014Z; dd_custom.ts14={%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221670025600%22:56}}; digi_uc=W1sidiIsIjYxMTg0NCIsMTY3MDA1MTg1MjE4M10sWyJ2IiwiMTQwMjE3IiwxNjcwMDQ5NDk3NDQyXSxbInYiLCI4MTA0NTkiLDE2NzAwNDI0MDA5OTRdLFsiY3YiLCIxNDAyMTciLDE2NzAwNTQ1NTY1NjJdLFsiY3YiLCI2ODc1MzMiLDE2NzAwNTQ1MzcyNzZdLFsiY3YiLCI2MjMzNTMiLDE2NzAwNDk5Mjc4MTJdLFsiY3YiLCI2NTYxNzIiLDE2NzAwNDk4OTMwNDldLFsiY3YiLCI2MzQwMzkiLDE2NzAwNDk4NDA3NTNdLFsiY3YiLCI5MjY4NzgiLDE2NzAwNDk4MTE1NDldLFsiY3YiLCIxMDE4NDUiLDE2NzAwNDk3Mzc5NzddLFsiY3YiLCIxMjY5MTYiLDE2NzAwNDg3MTU0OTJdLFsiY3YiLCI2NzI1MzAiLDE2NzAwNDgwMzcwNTRdLFsiY3YiLCIxNTA5NjYiLDE2NzAwNDM5NDI1MzBdLFsiY3YiLCIxMDgyMDgiLDE2NzAwNTQ4NDI4MDVdXQ==; u__geoCityGuid=bd10887b-2da4-11df-942d-0023543d7b52; _ga=GA1.2.1071695914.1670042092; __tld__=null; dd__lastEventTimestamp=1670059396857; mindboxDeviceUUID=14c3907a-f9ad-49d9-9d07-6de00b365e20; directCrm-session=%7B%22deviceGuid%22%3A%2214c3907a-f9ad-49d9-9d07-6de00b365e20%22%7D; _ga_XW7S332S1N=GS1.1.1670059181.3.1.1670059603.60.0.0; qrator_msid=1670066563.151.TaCqUhCQudb7FOL9-nqdlqo0q8sgoudbnk153l2nsvv2ou9ke'

шапка = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'cookie': следы
}

запрос_к_городам = 'https://api.petrovich.ru/geobase/v1.1/cities?city_code=spb&client_id=pet_site'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def получаем_жсон_словарь(ссылка):
    ответ_запроса = session.get(ссылка, headers=шапка)
    словарь_жсон = json.loads(ответ_запроса.text)
    return словарь_жсон


def получить_кода_городов(строка_запроса):
    print("Получение списка городов")

    города_жсон_словарь = получаем_жсон_словарь(строка_запроса)

    большие_города = города_жсон_словарь['data']['commonCities']
    малые_города = города_жсон_словарь['data']['regionalCities']
    все_города = большие_города + малые_города

    рф_города = []
    коды_городов = {}
    for город in все_города:
        if город['code'] == 'rf':
            рф_города.append(город['title'])
            continue
        коды_городов[город['code']] = город['title']
    коды_городов['rf'] = ', '.join(рф_города)
    return коды_городов


def получить_категории_для_города(код_города):
    print("Обработка города:", код_города)

    # https://api.petrovich.ru/catalog/v2.3/sections/tree/3?city_code=rf&client_id=pet_site
    запрос_к_категориям = 'https://api.petrovich.ru/catalog/v2.3/sections/tree/3'

    парамерты = {
        'city_code': код_города,
        'client_id': 'pet_site'
    }
    ответ_запроса = requests.get(запрос_к_категориям, headers=шапка, params=парамерты)
    словарь_жсон = json.loads(ответ_запроса.text)

    основные_категории = словарь_жсон['data']['sections']
    коды_категорий = []
    for над_категория in основные_категории:
        if 'sections' in над_категория and над_категория['sections']:
            for категория in над_категория['sections']:
                коды_категорий.append([категория['code'], код_города])
    return коды_категорий


def получить_категории_по_городам(коды_городов):
    категории_по_городам = []
    i = -1
    for код_города in коды_городов:
        i += 1
        if i == 1:  # количество городов для обработки
            break
        категории_по_городам.extend(получить_категории_для_города(код_города))

    return категории_по_городам


def получить_список_кодов_товаров_по_категории_и_городу(категория, код_города):
    print("Получение списка товаров для категории и города:", категория, код_города)

    global список_кодов_товаров

    # https://api.petrovich.ru/catalog/v2.3/sections/12101?limit=20&offset=0&city_code=spb&client_id=pet_site
    запрос_к_списку_товаров = 'https://api.petrovich.ru/catalog/v2.3/sections/'

    начальный_сдвиг = 0
    лимит_апи = 50

    парамерты = {
        'limit': лимит_апи,
        'offset': начальный_сдвиг,
        'city_code': код_города,
        'client_id': 'pet_site'
    }

    ответ_запроса = requests.get(запрос_к_списку_товаров + str(категория), headers=шапка, params=парамерты)
    словарь_жсон = json.loads(ответ_запроса.text)

    if словарь_жсон['state']['title'] != "ОК":
        print(bcolors.WARNING + "Запрос не выполнен" + bcolors.ENDC)
        print(словарь_жсон)
        return

    список_товаров = словарь_жсон['data']['products']
    количество_товаров = словарь_жсон['data']['pagination']['products_count']

    if количество_товаров > лимит_апи:
        while количество_товаров > лимит_апи:
            начальный_сдвиг += лимит_апи

            парамерты['offset'] = начальный_сдвиг

            ответ_запроса = requests.get(запрос_к_списку_товаров + str(категория), headers=шапка, params=парамерты)
            print(ответ_запроса.status_code, ответ_запроса.text[:1000])
            словарь_жсон = json.loads(ответ_запроса.text)

            if словарь_жсон['state']['title'] != "ОК":
                print(bcolors.WARNING + "Запрос не выполнен" + bcolors.ENDC)
                print(словарь_жсон)
                return

            список_товаров.extend(словарь_жсон['data']['products'])

            количество_товаров -= лимит_апи

    print("Получено:", len(список_товаров), 'товаров')

    return код_города, список_товаров


def записать_итог_асинхра_код_города_и_товары(итог):
    код_города = итог[0]
    товары = итог[1]

    for товар in товары:
        if код_города not in список_кодов_товаров:
            список_кодов_товаров[код_города] = []
        список_кодов_товаров[код_города].append(товар['code'])


def получить_список_всех_товаров(категории_по_городам_1):
    pool = Pool(10)

    начальное_время = time.time()

    список_кодов_всех_товаров = []
    i = -1
    for город_категория_спис in категории_по_городам_1:
        i += 1
        if i == 1:  # количество категорий для обработки
            break

        категория = город_категория_спис[0]
        город = город_категория_спис[1]

        pool.apply_async(получить_список_кодов_товаров_по_категории_и_городу, (категория, город), callback=записать_итог_асинхра_код_города_и_товары)

        # список_кодов_всех_товаров.append(получить_список_кодов_товаров_по_категории_и_городу(категория, город))
        # записать_данные_товаров_по_городу(город, список_товаров)

    pool.close()
    pool.join()

    print("--- %s секунд ---" % (time.time() - начальное_время))


def записать_коды_товаров(список_кодов_товаров):
    if not os.path.exists(папка_для_кодов_товаров):
        os.makedirs(папка_для_кодов_товаров)

    общее_товарных_кодов = 0
    for код_города in список_кодов_товаров:
        список_товарных_кодов = список_кодов_товаров[код_города]

        общее_товарных_кодов += len(список_товарных_кодов)

        with open(папка_для_кодов_товаров + '/' + str(код_города) + '.txt', 'w') as f:
            for код in список_товарных_кодов:
                f.write(str(код) + '\n')
    print("Собрано товаров: ", общее_товарных_кодов)


def получить_данные_на_товар(код_товара, код_города):
    global список_товаров

    парамерты = {
        'city_code': код_города,
        'client_id': 'pet_site'
    }

    # https://api.petrovich.ru/catalog/v2.3/products/код_товара?city_code=код_города&client_id=pet_site
    запрос_к_товару = 'https://api.petrovich.ru/catalog/v2.3/products/'

    ответ_запроса = requests.get(запрос_к_товару + str(код_товара), headers=шапка, params=парамерты)
    словарь_жсон = json.loads(ответ_запроса.text)

    if словарь_жсон['state']['title'] != "ОК":
        print(bcolors.WARNING + "Запрос не выполнен" + bcolors.ENDC)
        print(словарь_жсон)
        return

    товар = словарь_жсон['data']['product']

    print("Загрузка товара:", код_товара, len(список_товаров))

    return [код_города, товар]


def взять_данные_из_товара(код_товар_спис):
    код_города = код_товар_спис[0]
    товар = код_товар_спис[1]
    данные_товара = {
        'code': товар['code'],
        'city_code': код_города,
        'city': коды_городов[код_города],
        'title': товар['title'],  # название товара
        'category_title': товар['section']['title'],  # категория товара
        'description_no_html': товар['description_no_html']['description'],  # описание товара
        'weight': товар['weight'],  # вес
        'height': товар['height'],  # высота
        'length': товар['length'],  # длина
        'width': товар['width'],  # ширина
        'unit_title': товар['unit_title'],  # "шт"
        'unit_ratio': товар['unit_ratio'],
        'unit_ratio_alt': товар['unit_ratio_alt'],  # "пог. м"
        'unit_title_alt': товар['unit_title_alt'],
        'increment_step': товар['increment_step'],

        # цена
        'price': товар['price'],  # список

        # характеристики товара
        'properties': товар['properties'],  # список

        # изображения
        'images': товар['images'],  # список

        # категории товара
        'breadcrumbs': товар['breadcrumbs'],  # список

        # дополнительное описание товара
        'extended_description_no_html': товар['extended_description_no_html'],  # список
    }
    return данные_товара


def записать_товары(код_города):
    global список_товаров

    if not os.path.exists(папка_для_товарных_данных):
        os.makedirs(папка_для_товарных_данных)

    with open(папка_для_товарных_данных + '/' + str(код_города) + '.csv', 'w', encoding="utf-8", newline='') as файл:
        записчик = csv.writer(файл, delimiter=';')
        первая_строка_для_цсв = list(взять_данные_из_товара(список_товаров[0]).keys())
        записчик.writerow(первая_строка_для_цсв)

        for товар in список_товаров:
            данные_товара = взять_данные_из_товара(товар)
            значения = []
            for значение in данные_товара.values():
                значения.append(значение)
            if значения:
                записчик.writerow(значения)


def записать_итог_асинхра_данные_товаров(итог):
    список_товаров.append(итог)


def получить_товары_по_городам():
    print("Количество городов:", len(список_кодов_товаров))

    for код_города in список_кодов_товаров:
        pool_2 = Pool(10)
        начальное_время = time.time()

        коды_товаров = список_кодов_товаров[код_города]
        i = -1
        for код_товара in коды_товаров:
            i += 1
            if i % 100 == 0:
                print(f"Обработано {i} товаров данного города")
            pool_2.apply_async(получить_данные_на_товар, (код_товара, код_города),
                               callback=записать_итог_асинхра_данные_товаров)

        print("--- %s секунд Загрузка данных товаров одного города---" % (time.time() - начальное_время))

        pool_2.close()
        pool_2.join()

        записать_товары(код_города)


папка_для_кодов_товаров = r'kody_tovarov'
папка_для_товарных_данных = r'tovary_po_gorodam'

список_кодов_товаров = {}

список_товаров = []

коды_городов = получить_кода_городов(запрос_к_городам)

категории_по_городам = получить_категории_по_городам(коды_городов)

получить_список_всех_товаров(категории_по_городам)

записать_коды_товаров(список_кодов_товаров)

получить_товары_по_городам()
