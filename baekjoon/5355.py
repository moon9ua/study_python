# t = int(input())

# lists = list(range(t))

# for i in range(t):
# 	lists[i] = list(input().split())

# def mars(ls):
# 	num = ls[0]
# 	i = 1
# 	while i < 

# 해보려고 했는데 이거 잘 안풀린다...


# t = int(input())

# for _ in range(t):		# _가 뭐지..? i같은건가?
# 	mars = list(map(str, input().split()))		# 왜 str로 하지?
# 	num = 0
# 	for i in range(len(mars)):
# 		if i == 0:
# 			num = num + float(mars[i])
# 		else:
# 			if mars[i] == "#":
# 				num = num - 7
# 			elif mars[i] == "%":
# 				num = num + 5
# 			elif mars[i] == "@":
# 				num = num * 3
# 	print("%0.2f" % num)	# 소수점 나타내는 방식 배우자.

# 한번에 입력받아서 한번에 출력하는거 구현하고 싶음...
# 이건 정확한 정답이 아닌 것 같다.


t = int(input())
lists = list(range(t))

for i in range(t):
	lists[i] = list(input().split())	# 리스트의 요소가 리스트.

for i in range(t):
	num = 0
	for j in range(len(lists[i])):
		if j == 0:
			num = num + float(lists[i][j])		# 이중배열 처음 해봤는데 되네.
		else:
			if lists[i][j] == "#":
				num = num - 7
			elif lists[i][j] == "%":
				num = num + 5
			elif lists[i][j] == "@":
				num = num * 3
	print("%0.2f" % num)

# 아직 정확히 이해는 안되지만 구현은 함! 원하던게 이거임!