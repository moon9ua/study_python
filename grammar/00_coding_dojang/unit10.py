# Unit 10. 리스트와 튜플 사용하기


# <리스트>

# a = [1,2,3,4,5]
# 리스트. 요소(element).

# person = ['james', 10, 2.5, True]
# 여러 자료형 저장 가능.

# a = []
# b = list()
# 빈 리스트 생성.

# range(10)
# a = list(range(10))	# 0~9까지 들어있는 리스트.
# b = list(range(5, 12))	# 5~11까지 들어있는 리스트.
# c = list(range(-4, 10, 2))	# 증가폭이 2.
# d = list(range(10, 0, -1))	# 증가폭이 -1.


# <튜플>

# a = (1,2,3,4,5)
# 튜플. 튜플은 각 요소를 변경, 추가, 삭제 할 수 없음. 읽기 전용 리스트.

# person = ('james', 10, 1.5, True)

# (38,)		# (38)하면 그냥 값이 되어버림.
# 38,	# 이렇게도 튜플 가능.
# 요소가 한개인 튜플.

# a = tuple(range(10))
# b = tuple(range(5, 12))
# c = tuple(range(-4, 10, 2))

# a = [1,2,3]; tuple(a)
# b = (4,5,6); list(b)

# cf) 리스트와 튜플 안에 문자열이 들어가면?
# list('hello'); tuple('world')

# cf) 리스트와 튜플로 변수 만들기.
# 는 귀찮아서 안읽음.


# <연습문제>

a = list(range(5, -10, -2))
print(a)