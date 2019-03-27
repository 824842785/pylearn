while 1 == 1:     #程序一直运行
	a = int(input("输入一个小于80的正奇数"))

	while a > 80:
		a= int(input("不在范围之内,请重新输入一个小于80的正奇数"))

	while a % 2 == 0:
		a = int(input("输入为偶数,请重新输入一个小于80的正奇数"))
	
	b = int(input("请输入一个小于第一个数的数"))

	while b >= a:
		b = int(input("请输入一个小于第一个数的数"))
	
	e= str(input("输入一个符号"))
	f= str(input("再输入一个符号"))
	
	r = (a + 1) // 2 

	def print1(c,d,*address):
		for g in address:
			for i in range(1,r):
				for j in range(r - i):
					print (' ',end='')
				if i < d+0.5:	
					print ((2*i-1)*g)
				else:
					print (d * g + (2*(i - d)-1) * ' ' + d * g)

			for i in range(r):
				for j in range(i):
					print (' ',end='')
				if i < r-d-0.5:
					print (d*g+ (a-2*d-2*i)*' '+ d*g)
				else:
					print ((a-2*i)*g)
			
	 
	print1(a,b,e,f)
	