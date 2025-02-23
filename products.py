products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
	#上一行是減縮寫法，原始寫法如下
	# p =[]
	# p.append(name)
	# p.append(price)
	# prosucts.append(p)

print(products)

for p in products:
	print(p[0], '的價格是:', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')