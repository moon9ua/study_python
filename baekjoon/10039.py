a = list(range(5))

for i in range(5):
	a[i] = int(input())
	if a[i] < 40:
		a[i] = 40

print(int(sum(a)/len(a))) # int() # sum() # len()

