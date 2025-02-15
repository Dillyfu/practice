import random
start = input('請輸入隨機猜字最小值')
end = input('請輸入隨機猜字最大值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字:')
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