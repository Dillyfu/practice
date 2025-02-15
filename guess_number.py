import random

r = random.randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('猜1至100一個數字:')
	num = int(num)
	if num == r:
		print('答對了!')
		print('已經猜', count, '次')
		break
	elif num > r:
		print('再猜小一點')
	elif num < r:
		print('再猜大一點')
	print('已經猜', count, '次')