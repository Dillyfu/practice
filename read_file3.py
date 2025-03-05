lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f: # 檔案 f 裡面的每一行，加進 line 清單
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5] # 當資料連在一起時，無法用split(' ')分割時，可以用清單分割法，來把她取出
	name = s[0][5:]
	print(name)