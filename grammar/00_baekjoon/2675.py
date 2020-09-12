t = int(input())
r = list(range(t))
s = list(range(t))

for i in range(t):
	r[i], s[i] = input().split()

for i in range(t):
	for j in range(len(s[i])):
		for k in range(int(r[i])): # for문에서 range(int형) 의 형식이 헷갈렸음.
			print(s[i][j], end='')
	print()		# 개행의 위치가 약간 까다로웠음.

