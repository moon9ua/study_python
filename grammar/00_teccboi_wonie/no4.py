# https://youtu.be/cgsJC3Pp5K0
# 변수, 타입, 조건문, 함수

# <변수>
# x = 1; y = 2; print(x); print(y)
# z = "안녕"; print(z)


# <타입>
# 숫자
# x = 1; y = 2; z = 1.2
# print(x+y); print(x-y); print(x*y)
# print(x**y); print(x%y)

# 문자열
# x = 'hello'; y = "world"; print(x); print(y)
# z = """안녕하세요 워니입니다"""; print(z)
# print("안녕" + "잘지내니")
# print("몇살이니" + 4)	# 타입 안맞아서 에러
# print("몇살이니" + str(4))
# x = 4; y = "5"; print(x+y); print(str(x)+y); print(x+int(y))

# 불리안(boolean)
# x = True; y = False; print(x); print(y)


# <조건문>
# if 2 > 1:
# 	print('hello')

# if not 1 > 2:
#	print('hi')

# if 1 > 0 and 2 > 1:
# 	print("hello")

# if 0 > 0 or 2 > 1:
# 	print("hi")

# x = 3
# if x > 5:
# 	print("hello")
# elif x == 3:
# 	print("world")
# else:
# 	print("hi")


# <함수>
# print("철수: 안녕? 몇살이니")
# print("영희: 나는 20")
# print("철수: 안녕? 몇살이니")
# print("영희: 나는 20")

# def chat():
# 	print("철수: 안녕? 몇살이니")
# 	print("영희: 나는 20")
# chat()
# chat()

# def chat(name1, name2, age):
# 	print("%s: 안녕 몇살이니" % name1)
# 	print("%s: 나는 %d" % (name2, age))
# chat("알렉스", "윤하", 10)
# chat("철수", "영희", 20)

# a = 1; b = 2; c = a+b
# x = 1; y = 2; z = x+y

# def dsum(a, b):
# 	result = a + b
# 	return result
# d = dsum(1,2)
# print(d)


# <복습>
# 이름과 나이를 받아라
# 나이가 10살 미만이면 '안녕'
# 나이가 10살에서 20살 사이면 '안녕하세요'
# 그 외에는 '안녕하십니까'

def sayhello(name, age):
	if age < 10:
		print('안녕, ' + name)
	elif age <= 20 and age >= 10:
		print('안녕하세요, ' + name)
	else:
		print('안녕하십니까, ' + name)

sayhello("구아", 5)
sayhello('철수', 15)
sayhello('영희', 25)