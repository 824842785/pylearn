import genranstr

maxlen=int(input('请输入一个数字'))
e=[]
for i in range(15):
	a=genranstr.genRanStr(maxlen)
	e.append(a)

print (e)
def statisticsElement(strs):
	D= dict.fromkeys(['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],0)
	for word in D:
		for m in range(len(strs)):
			D[word]+=strs[m].count(word)
		print (word,':',D[word])
	print (D)

statisticsElement(e)


		



	
