# 031
a = "3"
b = "4"
print (a + b) # 문자열 더하기

# 032
print ("HI" * 3) # 문자열 곱하기

# 033
print ("-" * 80)

# 034
t1 = 'python'
t2 = 'java'
ret = t1 + ' ' + t2 + ' '
print (ret * 4)

# 035
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print ("이름: %s 나이: %d" % (name1, age1))
print ("이름: %s 나이: %d" % (name2, age2)) # % 포맷

# 036
print ("이름: {} 나이: {}".format(name1, age1))
print ("이름: {} 나이: {}".format(name2, age2)) # .format()

# 037
print (f"이름: {name1} 나이: {age1}")
print (f"이름: {name2} 나이: {age2}") # f-스트링

# 038
상장주식수 = "5,969,782,550"
rep = 상장주식수.replace(",", "")
ret = int(rep)
print (ret)

# 039
분기 = "2020/03(E) (IFRS연결)"
ret = 분기.split("(")
print (ret[0])
print (분기[:7])

# 040
data = "   삼성 전자    "
# print (data.replace(" ", "")) # 문자열 내의 공백도 변환돼버림.
print (data.strip()) # .strip() replace와 마찬가지로 새로운 문자열 반환