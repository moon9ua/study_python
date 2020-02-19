n = int(input())

# for i in range(n): # i가 실제로 증가하는게 아니면, 중첩 for문에서 다 i로 써도 되나?
# 	if i > 1 and n % i == 0: # &&이 안되네? &은 되나?
# 		print(i)
# 		n = n / i # 이렇게하면 반복문에서 n 이 바뀐건데 어떻게될까..
# 		i = 0
# n이 잘 바뀌는지도 모르겠고, i가 초기화가 잘 안됨.

i = 2
while i <= n:
	if i >= 2 and n % i == 0:
		print(i)
		n = n/i
		# print("n: %d" % n)
		i = 0
	i = i + 1
