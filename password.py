pwd = 'a123456'
i = 3
while i > 0:
    password = input('請輸入使用者密碼: ')
    if pwd == password:
    	print('登入成功')
    	break #逃出迴圈
    else:
    	i -= 1
    	print('密碼錯誤! 還有',i,'次機會')
    	if i == 0:
    		print('拒絕存取')
    		break
    	

