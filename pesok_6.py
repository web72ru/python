def чётные(func):
	def исполнение(количество):
		список = func(количество)
		чётные = список[::2]
		return чётные 
	return исполнение

@чётные
def список(количество):
	список = list(range(0, количество))
	return список
	
print(список(20))