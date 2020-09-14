# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了！"
# 猜錯的話　要告訴他比答案大／小
import random
r = random.randint(1, 100)
n = 0
while n != r:
	n = input('請猜1-100的數字,請輸入數字:')
	n = int(n)
	if n > r:
		print('你的數字比答案大')
	elif n < r:
		print('你的數字比答案小')
print('猜到了數字為', n)
		#else
		#	print('猜到了數字為', n)
		#	break


