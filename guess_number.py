import random

r = random.randint(1,100)
while True:
	num = input('猜1至100一個數字:')
	num = int(num)
	if num == r:
		print('答對了!')
		break
	elif num > r:
		print('再猜小一點')
	elif num < r:
		print('再猜大一點')