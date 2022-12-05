import requests, lxml.html, json, csv, os

session = requests.Session()

ссылки_на_товары = ['https://api.petrovich.ru/catalog/v2.3/products/105679?city_code=rf&client_id=pet_site',
                    'https://api.petrovich.ru/catalog/v2.3/products/170127?city_code=rf&client_id=pet_site']
шапка = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2500 Yowser/2.5 Safari/537.36',
    'cookie': 'u__geoUserChoose=1; SIK=dwAAANh36ww4WagSnbACAA; SIV=1; C_sgOPYNA7JhUfgsBzMymLES3L2NY=AAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D8AAADnDtTpQc7uoVH1sQmkBREUduq9Qms; _gcl_au=1.1.413263012.1670006809; _ym_uid=16700068091042586788; _ym_d=1670006809; tmr_lvid=b3e57d4243b4a3562f144012268dcf64; tmr_lvidTS=1670006809514; _gid=GA1.2.1401508863.1670006810; _ym_isad=1; ssaid=ae975e60-7271-11ed-ba7a-0bd6a8f7d83f; UIN=dwAAAC_19EUYjz4NhBKCQlbzTWEJSWdcOlmoEgo4AAA; rrpvid=939403301467498; rcuid=638a4815ff40ea423fad7f60; aplaut_distinct_id=wS34rLv3QNzP; popmechanic_sbjs_migrations=popmechanic_1418474375998=1|||1471519752600=1|||1471519752605=1; SNK=125; u__typeDevice=desktop; dd_user.isReturning=true; u__geoCityGuid=2379592f-c532-11e7-ad18-00259038e9f2; _ga=GA1.2.989252348.1670006809; dd_custom.lt13=2022-12-03T07:56:05.817Z; dd_custom.ts14={"ttl":2592000,"granularity":86400,"data":{"1669939200":56,"1670025600":8}}; _ga_XW7S332S1N=GS1.1.1670049620.4.1.1670054168.50.0.0; dd__persistedKeys=["custom.lastViewedProductImages","custom.lt13","custom.ts14","custom.ts12","custom.lt11","user.isReturning","custom.productsViewed"]; dd_custom.lastViewedProductImages=["","12716","18363"]; dd_custom.ts12={"ttl":2592000,"granularity":86400,"data":{"1669939200":5,"1670025600":4}}; dd_custom.lt11=2022-12-03T07:56:08.978Z; __tld__=null; rrviewed=611119,611844,105679; dd__lastEventTimestamp=1670054169017; digi_uc=W1sidiIsIjYxMTg0NCIsMTY3MDA1MTI4MjE4Ml0sWyJ2IiwiNjExMTE5IiwxNjcwMDQ5NzE0MTI0XSxbInYiLCIxMjY5MTYiLDE2NzAwMDkzNDE2MjZdLFsiY3YiLCIxMDU2NzkiLDE2NzAwNTQxNjQ5NDBdLFsiY3YiLCI2NTkyODYiLDE2NzAwNTQxNTk5MDddLFsiY3YiLCIxMDgyMDgiLDE2NzAwNDk2NDMwMzhdLFsiY3YiLCIxMDE4NDUiLDE2NzAwNDk2MjQxODVdLFsiY3YiLCI2Mjg2NzkiLDE2NzAwNDY5MjkzNTZdLFsiY3YiLCI4MDE2MjgiLDE2NzAwNDY5MDQyOTZdLFsiY3YiLCI3Nzk0NjkiLDE2NzAwNDY4MjI4NDJdLFsiY3YiLCI5MDg1MzciLDE2NzAwNDU3MDM4ODddLFsiY3YiLCIxNDI2NTgiLDE2NzAwMjAxMTc2MTldLFsiY3YiLCI4ODU3ODUiLDE2NzAwMTgyNjE3MzhdLFsidiIsIjEwNTY3OSIsMTY3MDA1NDE2ODY1N11d; rrlevt=1670054169209; mindboxDeviceUUID=3060136d-af14-4f65-a306-9fb5ea4ae685; directCrm-session={"deviceGuid":"3060136d-af14-4f65-a306-9fb5ea4ae685"}; qrator_msid=1670049618.523.0yKBotlNGg1P6fya-qm6jbjrquvpmvttbg0ofd69ud2ooacmo'

}

CSV = 'petrovich.ru.csv'


def получаем_хтмл(ссылка):
    хтмл = session.get(ссылка, headers=шапка)
    return хтмл


def получаем_данные_товара(список_ссылок):
    ключи = ['название', 'изы', 'главная иза', 'категории', 'вес', 'высота', 'длина', 'ширина', 'цена1', 'цена2',
             'цена3', 'цена4', 'количество', 'описание', 'ссылка']

    for ссылка in список_ссылок:
        значения = []
        страница = получаем_хтмл(ссылка)
        содержимое_страницы = страница.text
        словарь = json.loads(содержимое_страницы)

        ключи_словарь = словарь['data']['product']
        ключи_список = list(словарь['data']['product'].keys())
        значения_список = list(словарь['data']['product'].values())

        значения.append(ключи_словарь['title'])  # название
        значения.append(ключи_словарь['images'])  # изы
        значения.append(ключи_словарь['cover_image'])  # главная иза

        категории = []
        for категория in ключи_словарь['breadcrumbs']:
            категории.append(категория['title'])
        значения.append(категории)  # категории

        значения.append(ключи_словарь['weight'])  # вес
        значения.append(ключи_словарь['height'])  # высота
        значения.append(ключи_словарь['length'])  # длина
        значения.append(ключи_словарь['width'])  # ширина
        значения.append(ключи_словарь['price']['gold'])  # цена1
        значения.append(ключи_словарь['price']['retail'])  # цена2
        значения.append(ключи_словарь['price']['points'])  # цена3
        значения.append(ключи_словарь['price']['individual'])  # цена4
        if ключи_словарь['remains']['supply_ways']:
            значения.append(ключи_словарь['remains']['supply_ways'][0]['total'])  # колчество
        значения.append(ключи_словарь['description'])  # описание
        значения.append(ключи_словарь['link'])  # ссылка

        

        print(ключи)
        print(значения)

    with open(CSV, 'w', newline='') as файл:
        записчик = csv.writer(файл, delimiter=';')
        записчик.writerow(значения)


получаем_данные_товара(ссылки_на_товары)
