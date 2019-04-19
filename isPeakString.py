import genranstr

D= dict.fromkeys(['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],0)
i=0
for word in D:
	D[word]+=i
	i+=1

maxlen=int(input('请输入一个数字'))
a=genranstr.genRanStr(maxlen)
#print (a)
#a='abcdef'
if len(a)>= 3:
	e=[]
	for m in range(1,len(a)-1):
		if D[a[m]] > D[a[m-1]] and D[a[m]] > D[a[m+1]]:
			e.append(a[m])
			n=m
	if len(e) == 1:
		print ('maxword is',a[n])
		for i in range(n-1):
			if D[a[i]] <=D[a[i+1]]:
				o=1
			else:
				o=0
				break
		if  n>= len(a)-1:
			print (a)
		else :
			for j in range(n,len(a)-1):
				if D[a[j]] >= D[a[j+1]]:
					p=1
				else:
					p=0
					break
		if (o== 1 and p == 1):
			print (a)
		else:
			print(a,'is not isPeakString')
	else:
		print (a,'is not isPeakString')
else:
	print (a,'is not isPeakString')
			
	
			
			
		



	
