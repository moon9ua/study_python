# 252
# class Human:
#     pass # 비어있는 클래스를 뜻하나?

# 253
# areum = Human() # 인스턴스 생성

# 254
# class Human:
#     def __init__(self): # 생성자
#         print("응애응애")
# areum = Human()

# 255
# class Human:
#     def __init__(self, name, age, sex): # 생성자
#         self.name = name
#         self.age = age
#         self.sex = sex
# areum = Human("아름", 25, "여자")
# print(areum.name)

# 256
# class Human:
#     def __init__(self, name, age, sex): # 생성자
#         self.name = name
#         self.age = age
#         self.sex = sex
# areum = Human("아름", 25, "여자")
# print("이름: %s, 나이: %d, 성별: %s" % (areum.name, areum.age, areum.sex))

# 257
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self): # 메소드
#         print("이름: %s, 나이: %d, 성별: %s" % (self.name, self.age, self.sex))

# areum = Human("아름", 25, "여자")
# areum.who()

# 258
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def who(self): # 메소드
#         print("이름: %s, 나이: %d, 성별: %s" % (self.name, self.age, self.sex))

#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("모름", 0, "모름")
# areum.who()
# areum.setInfo("아름", 25, "여자")
# areum.who()

# 259
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self): # 소멸자
        print("나의 죽음을 알리지 말라")

    def who(self): # 메소드
        print("이름: %s, 나이: %d, 성별: %s" % (self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("모름", 0, "모름")
areum.setInfo("아름", 25, "여자")
areum.who()
del areum
# areum.who() # 이미 삭제돼서 오류.