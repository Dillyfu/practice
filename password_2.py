password = 'abcd1234'
i = 3 #剩餘機會
while i > 0:
	pwd = input('請輸入密碼: ')
    if pwd == password:
    	print('登入成功!!')
    	break #結束迴圈
    else:
    	i = i - 1
    	print('密碼錯誤! 還有', i, '次機會')
    	