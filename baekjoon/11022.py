t = int(input())

a = list(range(t))
b = list(range(t))

for i in range(t):
	a[i], b[i] = map(int, input().split())

for i in range(t):
	print("Case #%d: %d + %d = %d" % (i+1, a[i], b[i], a[i]+b[i]))