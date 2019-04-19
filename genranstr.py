def genRanStr(maxlen):
	import random
	random_str = ''
	base_str = 'abcdefghigklmnopqrstuvwxyz'
	length = len(base_str) - 1
	for i in range(random.randint(0,maxlen)):
		random_str += base_str[random.randint(0, length)]
	return random_str
