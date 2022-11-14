txt = 'Сегодня 14.11.2022'
spis = txt.split(' ')
data = []
for i in spis:
	s = i.split('.')
	for z in s:
		d = z.isdigit()
		if d == True:
			data.append(z)

print (f'Число: {data[0]} Месяц: {data[1]} Год: {data[2]}')