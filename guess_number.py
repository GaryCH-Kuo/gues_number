import random
r = random.randint(1, 100)
x = 10
while x > 0 :
	x = x - 1
	num = input('請猜出終結數字:')
	num = int(num)
	if num == r:
		print('你猜中了!!!')
		break
	elif num > r:
		print('比終結數字大')
	elif num < r:
		print('比終結數字小')
		if x == 0:
			print('幹，給你10次機會還猜不對!!!你是豬阿!!!')
