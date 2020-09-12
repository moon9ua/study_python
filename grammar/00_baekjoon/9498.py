grade = int(input())

if 90 <= grade <= 100: # C에선 이거 안됐던 것 같은데, 파이썬에선 되네.
	print("A")
elif 80 <= grade <= 89:
	print("B")
elif 70 <= grade <= 79:
	print("C")
elif 60 <= grade <= 69:
	print("D")
else:
	print("F")
