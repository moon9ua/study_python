# 241
import datetime
print(datetime.datetime.now())

# 242
now = datetime.datetime.now()
print (type(now))

# 243
for i in range(5, 0, -1):
    delta = datetime.timedelta(i)
    date = now - delta
    print (date)

# 244
# 풀다가 말음.