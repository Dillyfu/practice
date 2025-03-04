# with 讀取檔案
def read_file(filename): # 把檔名設為參數:filename，使用function函式時再決定用哪個檔案
	data = []  # 名為data的空清單
	with open(filename, 'r', encoding='utf-8-sig') as f: 
	# with 是python 獨有的自動檔案關閉功能
	# r 代表 read 讀取
	# 因為編碼中有中文，在語法中加入utf-8編碼，才能讀取中文檔案
	# 在存記事本，標頭出現諸如 \ufeff 等字串是有關編碼的資料，將utf-8 改 utf-8-sig 可取消之
	# as 當作
	# 檔案 f (代字，可自訂)
		for line in f: 
			# for 迴圈:把清單中的東西 一個個拿出來
			# 每一行取名為 line
			data.append(line.strip())  # 將每一行加入data空清單中
			# strip() 是把換行符號或多餘的空格去掉，只能對字串做
			# 將每一行用 strip() 把換行符號去掉後，加入data空清單中
	return data # 回傳

# 轉換對話紀錄
def convert(data):
	new = []
	person = None # 將 person 先設成無，以排除"當第一行不是人名時"，程式當掉風險
	allen_word_count = 0 # 創造變數
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0 # 創造變數
	viki_sticker_count = 0
	viki_image_count = 0
	for line in data: # 一行行讀取 data 清單
		s = line.split(' ') # 每一行用 split() 切割，以空白切割
		time = s[0] # 清單中 時間在第一項
		name = s[1] # 清單中 人名在第二項
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1 # 將1累加上去
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]: # 清單中第三項以後
					allen_word_count += len(m) # += 是累加，len 是計數
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1 # 將1累加上去
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]: # 清單中第三項以後
					viki_word_count += len(m) # += 是累加，len 是計數
					
	print('Allen說了', allen_word_count, '個字, 傳了', allen_sticker_count, '個貼圖及', allen_image_count, '張圖片')
	print('Viki說了', viki_word_count, '個字，傳了', viki_sticker_count, '個貼圖及', viki_image_count, '張圖片')


		# print(s) # 先印出
	return new # 將 轉換好的對話紀錄回傳出來


def write_file(filename, data): # 把要寫入檔案的東西放進，有檔名及要寫入的資訊
	with open(filename, 'w') as f: # 
		for line in data: # 一行行讀取 data 清單
			f.write(line + '\n') # f 檔案的寫入功能，將'每一行'與'換行符號' 都寫入



def main():			
	data = read_file('LINE-Viki.txt') 
	data = convert(data) # 將 convert 過的 data 再存入 data
	# write_file('output.txt', data)
	


main() # 使用 main() 才能進入主要程式碼，也係程式進入點 @atat