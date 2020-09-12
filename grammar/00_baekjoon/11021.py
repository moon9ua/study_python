# t = int(input())

# i = 0
# while i < t:
# 	a, b = map(int, input().split())
# 	print('Case #%d: %d' %(i, a+b))
# 	i = i + 1

## 다 입력받고 마지막에 출력하는 것이 정확한 답 아닐까? 그건 어떻게 할까...?
## 변수명에 i를 들어가게, 예를 들어 a_i, b_i들로는 저장 못하나?
## 아마 리스트같은걸 사용해서 한번에 출력하게 할 수 있을 것 같다.


t = int(input())

a = list(range(t))	
b = list(range(t))

i = 0
while i < t:
	a[i], b[i] = map(int, input().split())
	i = i + 1

i = 0
while i < t:
	print("Case #%d: %d" %(i+1, a[i]+b[i]))
	i = i + 1

## 한번에 나오도록 다시 풀어본 풀이.