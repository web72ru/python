import requests, lxml, re

сессия = requests.Session()
исходник = 'https://www.tyumen-city.ru/'
шапка = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36'
}
def получаем_хтмл(ссылка, params=''):
	хтмл_страницы = сессия.get(ссылка, headers=шапка, params=params)
	return хтмл_страница
	
хтмл_страницы = получаем_хтмл(исходник)
print(хтмл_страницы)