# function 函式/功能
# function 是用來【收納】程式碼的
# 他是個功能
# function 的好處是可以一直使用這功能，可以增加程式碼的重複使用性

def wash():  # def = define 定義 # wash 是 function name 定義功能名稱
	print('洗衣步驟一')
	print('洗衣步驟二')
	print('洗衣步驟三')
wash()

def wash(dry): # def = define 定義 # wash 是 function name 定義功能名稱 
# 一個參數 dry 是參數
	print('放入衣服')
	print('加洗衣精')
	print('加水')
	if dry:
		print('烘衣')
wash(True)  # 使用 function ，if dry is True, 印出烘衣
wash(False)

def wash(dry, water): # def = define 定義 # wash 是 function name 定義功能名稱 
# 多個參數: dry, water 是參數，寫在()裡
	print('放入衣服')
	print('加洗衣精')
	print('加水', water, '分滿')
	if dry:
		print('烘衣')
wash(True, 6)  # 使用 function
wash(False, 6)

def wash(dry=False, water=8): # def = define 定義 # wash 是 function name 定義功能名稱
	# 多個參數 dry=False, water=8 且 表示 參數可以有預設值，等號左右參數不須空格分開
	print('放入衣服')
	print('加洗衣精')
	print('加水', water, '分滿')
	if dry:
		print('烘衣')
wash(water=10)  # 使用 function

def add(x, y): # def = define 定義 # add 是 function name 定義功能名稱
	print(x + y)
add(3, 4)
add(50, 99)

def add(x=1, y=2):
	print(x + y)
add(y=6)

def add(x, y):
	return x + y  # 因為有 return 回傳，才能把 function 函式/功能 執行結果存下來
result = add(7, 11)
print(result)

def average(numbers):
	avg = sum(numbers) / len(numbers) # sum總數 /除以 len清單長度
	return avg 
	# 以上兩行可簡寫成 reture sum(numbers) / len(numbers)
a = average([1, 2, 3])
print(a)
# 以上兩行可簡寫成 print(average([1, 2, 3]))
print(average([6, 5, 99]))