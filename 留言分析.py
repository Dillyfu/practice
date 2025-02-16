data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 50000 == 0: # %代表求餘數
			print(len(data))
print('檔案計有:', len(data), '筆留言')
print(data[0])
print('----------------')
print(data[10])

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