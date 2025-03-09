# 一百萬筆留言中最常出現那些字
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 100000 == 0: # %代表求餘數
			print(len(data))
print('檔案計有:', len(data), '筆留言')
print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言字母數小於100')
print(new[0])
print(new[1])


amazing = []
for d in data:
	if 'amazing' in d:
		amazing.append(d)
print('一共有', len(amazing), '筆留言提到amazing')
print(amazing[0])

amazing = [d for d in data if 'amazing' in d] #清單快寫法
print(amazing)

#詢問bad有無在留言內，有就True 沒有就False
bad = []
for d in data:
	bad.append('bad' in d)

bad = ['bad' in d for d in data] #清單快寫法
print(bad)

# word_count 文字計數
wc = {}  # 定義空字典
for d in data:  # 一個個讀取 data 清單的留言檔，把每個留言是一個字串叫 d
	words = d.split()  # d 用空格切割 才能拿到每個字，words 是清單中裝著很多字，
	# 也可把split內的空格拿掉，避免字數統計把空格算入
	for word in words:  # 用另一個 for loop 來讀取 words 清單中的每個字 word
		if word in wc:
			wc[word] += 1  # 去 wc 字典中查找 word 出現次數，若出現，就累加
		else:
			wc[word] = 1  # 加入字典，新增新的 key 進 wc 字典

for word in wc:  #  字典中的每個 key 
	if wc[word] > 300:  # 
		print(word, wc[word])  #  把字印出，也把出現的次數印出

print(len(wc))  # 印出字典長度 就知字典中總共有幾個字
# print(wc['Burgess'])

while True:
	word = input('請問你想查什麼字?')
	if word =='q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('這個字沒出現過')
print('感謝你使用本查詢功能')

