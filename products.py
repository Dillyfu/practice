products = []
while True:  # while loop 用在不知道要執行幾次的地方
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)  # 把price變整數
	products.append([name, price])
	#上一行是減縮寫法，原始寫法如下
	# p =[]
	# p.append(name)
	# p.append(price)
	# prosucts.append(p)

print(products)

for p in products:
	print(p[0], '的價格是:', p[1])

with open('products.csv', 'w', encoding='utf-8') as f: # 避免產生亂碼，加入encoding='utf-8'
	f.write('商品,價格\n') # 加入欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  # 因 price 是整數，用 str() 轉換成字串