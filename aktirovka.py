import requests, lxml, re

исходник = 'https://www.tyumen-city.ru/'
шапка = {
	'accept': '*/*',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36'
}
def получаем_хтмл(ссылка, params=''):
	хтмл_страница = requests.get(ссылка, headers=шапка, params=params)
	return хтмл_страница
	
хтмл_страницы = получаем_хтмл(исходник)
print(хтмл_страницы)