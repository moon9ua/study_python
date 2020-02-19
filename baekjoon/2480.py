a = list(map(int, input().split()))
a = sorted(a)

if (a[0] < a[1] < a[2]):
	print(a[2] * 100)
elif (a[0] == a[1] == a[2]):	# 이게 되나?
	print(10000 + a[0] * 1000)
elif (a[0] == a[1] < a[2]):		# 이게 되나?
	print(1000 + a[0] * 100)
elif (a[0] < a[1] == a[2]):		# 사실 else로 해도 되긴함..
	print(1000 + a[1] * 100)