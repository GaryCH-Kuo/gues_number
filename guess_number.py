import random
start = input('請輸入隨機數字範圍開始值:')
start = int(start)
end = input('請輸入隨機數字範圍結束值:')
end = int(end)

r = random.randint(start, end)
x = 0
while True:
	x = x + 1
	num = input('請猜出終結數字:')
	num = int(num)
	if num == r:
		print('恭喜你猜中了!!!第', x,'次猜中')
		break
	elif num > r:
		print('比終結數字大')
	elif num < r:
		print('比終結數字小')
	print('已經猜了', x,'次!!!')