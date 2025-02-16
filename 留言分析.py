data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 10000 == 0: # %代表求餘數
			print(len(data))
print('檔案計有:', len(data), '筆留言')
print(data[0])
print('----------------')
print(data[10])

