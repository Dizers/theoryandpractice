try:
	time_road = int(input('Время в пути (в часах):'))
	time_rest = int(input('Время отдыха (в часах):'))
except ValueError:
	print('Error: Введите ЦЕЛОЕ ЧИСЛО!!')

time_begin = 7
time_end = 19

if time_road + time_rest >= 9 or time_road == 0:
	print('Всего рейсов 0')
else:
	sum_time = time_begin + time_road

	print(f'A {time_begin} - {sum_time} B')
	i = 0
	while sum_time <= (time_end - time_road - time_rest):
		time_begin = sum_time + time_rest
		sum_time = time_begin + time_road
		i += 1
		if i % 2 == 1:
			print(f'B {time_begin} - {sum_time} A')
		else:
			print(f'A {time_begin} - {sum_time} B')
	else:
		print(f'Всего рейсов: {i+1}')
