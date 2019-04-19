import genranstr
maxlen=int(input('请输入一个数字'))
e=[]
for i in range(15):
	a=genranstr.genRanStr(maxlen)
	print (a)
	e.append(len(a))

f=[]	
def statisticsLen(strs):
	for i in range (len(strs)):
		f.append(strs.count(i))
	print (f)

statisticsLen (e)

#print (e)

		



	
