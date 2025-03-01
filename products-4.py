# 檢查檔案在不在
import os # os = operating system


# 讀取檔案
def read_file(filename):
	products = [] # 不論有無找到檔案，都要產生空清單
	with open(filename, 'r', encoding='utf-8') as f: 
	# 寫入及讀取檔案都有編碼問題，要用同一種編碼，utf-8是一種常見編碼
		for line in f:
			if '商品,價格' in line: # 如果'商品,價格'在line 裡面的話，我就不處理，跳到下一回
				continue # 繼續 不會跳出迴圈，只是跳到下一回，使用時機，用在檔案讀取時
			name, price = line.strip().split(',') 
			# line 是字串，
			# strip 是把換行符號去掉
			# 用 split 來切割，括弧裡面輸入用什麼來當作切割的標準，每一行遇到逗點，就幫我切割
			products.append([name, price])
	return products # 回傳: 將讀完的資料回傳		
	

# 讓使用者輸入
def user_input(products):
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
	return products # 回傳: 將讀完的資料回傳


# 印出所有商品、價格
def print_products(products):
	for p in products:
		print(p[0], '的價格是:', p[1])


# 寫入檔案
def write_file(filename, products): 
	with open(filename, 'w', encoding='utf-8') as f: # 避免因編碼不對而產生亂碼，故加入編碼encoding='utf-8'
		f.write('商品,價格\n') # 加入欄位名稱
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')  # 因 price 是整數，用 str() 轉換成字串

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):  # os模組 的 path模組 的 isfile功能
		print('有此檔案')
		products = read_file(filename)
	else:
		print('無此檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()