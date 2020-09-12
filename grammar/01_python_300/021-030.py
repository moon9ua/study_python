# 021
letters = 'python'
print (letters[0], letters[2])

# 022
license_plate = "24가 2210"
print (license_plate[-4:])

# 023
string = "홀짝홀짝홀짝"
print (string[::2]) # 오프셋?

# 024
string = "PYTHON"
print (string[::-1]) # 오프셋?

# 025
phone_number = "010-1111-2222"
ret = phone_number.replace("-", " ") # .replace(<old>, <new>)
print (ret)

# 026
phone_number = "010-1111-2222"
ret = phone_number.replace("-", "") # .replace(<old>, <new>)
print (ret)

# 027
url = "http://sharebook.kr"
ret = url.split('.') # .split(<str>)
print (ret[-1])

# 028
# lang = 'python'
# lang[0] = 'P' # str은 수정 불가
# print (lang)

# 029
string = 'abcdfe2a354a32a'
ret = string.replace('a', 'A')
print (ret)

# 030
string = 'abcd'
string.replace('b', 'B')
print (string) # 'abcd' 출력. replace는 새로운 문자열을 리턴하는 것이기 때문.