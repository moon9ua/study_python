## https://youtu.be/orzUaKSndII
## 반복문

# print("철수: 안녕 뭐해")
# print("영희: 그냥 있어")
# print("철수: 안녕 뭐해")
# print("영희: 그냥 있어")
# print("철수: 안녕 뭐해")
# print("영희: 그냥 있어")

## 반복문에는 for, while이 있음.

# for i in range(3):
# 	print(i)	# 확인하기 위해 i 프린트. 당연 생략 가능.
# 	print("철수: 안녕 뭐해")
# 	print("영희: 그냥 있어")

# i = 0
# while i < 3:
# 	print(i)
# 	print("철수: 안녕 뭐해")
# 	print("영희: 그냥 있어")
# 	i = i + 1

## while이 더 편한 대표적 예: 무한루프
## while True 로 해놓으면 조건은 계속 지속.
## break와 continue를 통해 루프를 끝낸다.

## <break>

# i = 0
# while True:
# 	print(i)
# 	print("철수: 안녕 뭐해")
# 	print("영희: 그냥 있어")
# 	i = i + 1
# 	if i > 2:
# 		break

## for문으로는 이렇게 가능하긴 함.

# for i in range(100):
# 	print(i)
# 	print("철수: 안녕 뭐해")
# 	print("영희: 그냥 있어")
# 	i = i + 1
# 	if i > 2:
# 		break

## <continue>

# for i in range(3):
# 	print(i)
# 	print("철수: 안녕 뭐해")
# 	print("영희: 그냥 있어")
# 	if i != 2:
# 		continue
# 	print("워니: 어 얘들ㅇ...")