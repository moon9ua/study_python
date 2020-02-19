s = int(input())

sum = 0
i = 1

while (sum < s):
	sum = sum + i
	i = i + 1
	

if (sum == s):
	print(i-1) # 아.. 정확히 모르겠는데 그냥 10, 20만 직접 해보고 구한 값임.
else:
	print(i-2)