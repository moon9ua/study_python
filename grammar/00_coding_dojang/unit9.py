# <Unit 9. 문자열 사용하기>


##### 9.1 문자열 사용하기

# hello = '안녕하세요'; hello
# hello = "hello world!"; hello
# hello = '''hello world!!!!!'''; hello

# hello = '''hello
# world
# !!!'''
# print(hello)

# s = 'python isn't difficult!'		# 구문 에러(SyntaxError).
# s = "python isn't difficult!"		# ""를 사용하여 '를 문자로 처리했음.
# s = '''"안녕하세요" '파이썬입니다''''		# 여러줄 문자열에는 "와 '를 둘다 넣을 수 있음.

# cf) 문자열에 따옴표를 포함하는 다른 방법: 이스케이프 시퀀스
# 'python isn\'t difficult'

# 다른 cf는 귀찮아서 안읽음. 필요하면 사이트 참고...


##### 연습문제

s = '''Python is a programming language that lets you work quickly
and
integrate systems more effectively.'''

print(s)