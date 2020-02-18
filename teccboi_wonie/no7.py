## https://youtu.be/xdVt6qbghzI
## 클래스, 오브젝트

## 클래스: 함수+변수 모아놓은 것. 빵틀.
## 오브젝트: 클래스 써서 만든 것. 빵. instance.

# class Person:
# 	name = "워니"
# 	def say_hello(self):
# 		print("안녕. 나는 " + self.name)

# p = Person()
# p.say_hello()


# class Person2:
# 	def __init__(self, name):
# 		self.name = name
# 	def say_hello(self):
# 		print("안녕. 나는 " + self.name)

# wonie = Person2("워니")
# moon = Person2("문")
# jenny = Person2("제니")

# wonie.say_hello()
# moon.say_hello()
# jenny.say_hello()


# class Person2:
# 	def __init__(self, name):
# 		self.name = name
# 	def say_hello(self, to_name):
# 		print("안녕. " + to_name + " 나는 " + self.name)

# wonie = Person2("워니")
# moon = Person2("문")
# jenny = Person2("제니")

# wonie.say_hello("철수")
# moon.say_hello("영희")
# jenny.say_hello("희수")


class Person2:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def say_hello(self, to_name):
		print("안녕. " + to_name + " 나는 " + self.name)
	def introduce(self):
		print("내 이름은 " + self.name + " 나는 " + str(self.age) + " 살이야")

# wonie = Person2("워니", 20)
# wonie.introduce()


## <상속(inheritance)>
class Police(Person2):
	def arrest(self, to_arrest):
		print("넌 체포됐다. " + to_arrest)

class Programmer(Person2):
	def program(self, to_program):
		print("다음엔 뭘 만들지? 아 이걸 만들어야겠다: " + to_program)

wonie = Person2("워니", 20)
jenny = Police("제니", 15)
moon = Programmer("문", 22)

wonie.introduce()
jenny.introduce()	# 상속때문에 코드 없이도 person에 있는 함수 쓸 수 있음.
jenny.arrest("워니")
moon.introduce()
moon.program("이메일 클라이언트")
