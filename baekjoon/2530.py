hour, min, sec = map(int, input().split())
need_sec = int(input())

sec = sec + need_sec

if sec > 59:
	min = min + sec//60
	sec = sec%60	# 이걸 위에 하면, 이미 sec이 바껴있어서 에러.
if min > 59:
	hour = hour + min//60
	min = min%60
if hour > 23:
	hour = hour%24
print(hour, min, sec)