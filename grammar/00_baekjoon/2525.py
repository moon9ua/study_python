# from datetime import datetime, timedelta
# time1 = datetime.now()

## 원래는 시간 계산하는 패키지를 사용하려 했으나...
## 올림피아드 문제인 것을 보고 조건문을 이용하기로 함.

hour, min = map(int, input().split())
need_min = int(input())

min = min + need_min

if min > 59:
	hour = hour + min//60
	min = min%60
if hour > 23:
	hour = hour%24
print(hour, min)