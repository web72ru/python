txt = 'Сегодня 14.11.2022'
spis = txt.split(' ')
chisla = list(range(0,10))
print(chisla)
chisla = [str(x) for x in chisla]
print(chisla)
data_t = []
for znachenie in spis:
  if znachenie[0] in chisla:
    data_t = znachenie.split('.')
    break
den, mesiac, god = data_t
print (f'Число: {den} Месяц: {mesiac} Год: {god}')