# <Unit 8. 불과 비교, 논리 연산자 알아보기>


##### 8.1 불과 비교 연산자 사용하기

# True; False

# 3 > 1
# 10 == 10
# 10 != 5
# 'hello' == 'hello'
# 'Hi' == 'hi'
# 1 == 1.0		# True. '=='는 값 자체를 비교.
# 1 is 1.0		# False. 'is'는 객체를 비교.

# cf) 정수 객체와 실수 객체가 서로 다른 것은 어떻게 확인하나?
# id(1); id(1.0)	# 메모리 주소가 다름.

# cf) 값 비교에는 is를 쓰지마라.
# a = -5; a is -5
# a = -6; a is -6	# False. 변수 a가 있는 상태에서 할당해서 주소가 다름.


##### 8.2 논리 연산자 사용하기

# True and True
# True and False
# False and False	# 둘 다 True면 True.

# True or True
# True or False
# False or False	# 하나라도 True면 True.

# not True
# not False

# not True and False or not False	# True
# ((not True) and False) or (not False)		# 위 식이 이와 같음.

# 10 == 10 and 10 != 5
# 10 > 5 or 10 < 3
# not 10 > 5
# not 1 is 1.0

# cf) 정수, 실수, 문자열을 불로 만들기
# bool(1); bool(0)		# 0, 0.0을 제외한 모든 숫자는 True.
# bool(1.5); bool('False')		# ''을 제외한 모든 문자열은 True.

# cf) 단락 평가
# 너무 길어서 안읽음... 나중에 사이트 참고.


##### 8.4 연습문제

korean = 94
english = 47
math = 86
science = 81

print((korean >= 50) and (english >= 50) and (math >= 50) and (science >= 81))
# '=' 빼먹음.
