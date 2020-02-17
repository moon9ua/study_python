# <Unit 6. 변수와 입력 사용하기>


##### 6.1 변수 만들기

# x = 10; x
# y = 'hello!'; y

# type(x); type(y)

# x, y, z = 10, 20, 30;
# x; y; z

# x = y = z = 10; x; y; z

# x, y = 10, 20
# x, y = y, x
# c에서는 이런식으로 바로 바꿔줄 수 없을텐데, 파이썬에서는 값이 서로 바뀐다.

# cf) 변수 삭제하기
# x = 10; del x; x

# cf) 빈 변수 만들기
# x = None; x; print(x)


##### 6.2 변수로 계산하기

# a,b = 10,20; c = a+b; c

# a = 10; a+20; a;
# a = 10; a = a+20; a;
# b = 10; b +=20; b;

# cf) 부호 붙이기
# x = -10; +x; -x;


##### 6.3 입력 값을 변수에 저장하기

# input()
# x = input(); x
# x = input('문자열을 입력하세요:')
# (바로 문자열이 나오는데 이것을 프롬프트(prompt)라고도 함.)

# a = input(); b = input()
# a + b
# 10과 20을 입력했다면 '1020'이 나옴. 문자열이기 때문.
# type(a)

# a = int(input()); b = int(input()); a+b


##### 6.4 입력 값을 변수 두 개에 저장하기

# a, b = input('입력:').split(); a, b
# 공백을 기준으로 나누기때문에 공백 없으면 에러.

# a,b = input().split	# 공백 있어야함
# print(int(a)+int(b))
# a = int(a); b = int(b); a+b

# a,b = map(int, input().split()); a+b
# a,b = map(int, input().split(',')); a+b	# 콤마를 기준으로 분리.


##### 연습문제
a, b, c = map(int, input().split())
print(a+b+c)