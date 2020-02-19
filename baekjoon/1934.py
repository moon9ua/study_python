# t = int(input())
# a = list(range(t))
# b = list(range(t))
# num = list(range(t)) # 아 이게 좋은 방법은 아닌것같은데.. 대체법이 없을까.

# for i in range(t):
# 	a, b = map(int, input().split())
# 	if a > b:
# 		num = a
# 		while (True):
# 			if num % a == 0 and num % b == 0:
# 				break
# 			num = num + 1 # num++도 안되는것같던데 간략한 방법은?
# 	else:
# 		num = b
# 		while (True):
# 			if num % a == 0 and num % b == 0:
# 				break
# 			num = num + 1

# for i in range(t):
# 	print(num)

## 위 방법은 시간초과...


# t = int(input())

# a = list(range(t))
# b = list(range(t))
# num = list(range(t))

# for i in range(t):
# 	a, b = map(int, input().split())
# 	j = 2
# 	if a > b:
# 		num = a
# 		while (True):
# 			if num % b == 0:
# 				break
# 			num = a * j
# 			j += 1	# 이거 맞나?
# 	else:
# 		num = b
# 		while (True):
# 			if  num % a == 0:
# 				break
# 			num = b * j
# 			j += 1

# for i in range(t):
# 	print(num)

## 위 방법도 시간초과... 오래 걸려서가 아니라 뭔가 오류가 있어서 그런 것 같은데...


t = int(input())

for i in range(t):
	a, b = map(int, input().split())
	j = 2
	if a > b:
		num = a
		while (True):
			if num % b == 0:
				print(num)
				break
			num = a * j
			j += 1
	else:
		num = b
		while (True):
			if  num % a == 0:
				print(num)
				break
			num = b * j
			j += 1

## 시간초과가 떴었으나, pypy3으로 제출하여 성공. 이런...