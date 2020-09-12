# 121
# tmp = input()
# if tmp.islower():
#     print(tmp.upper())
# else:
#     print(tmp.lower())

# 124
# num1 = input("input number1: ")
# num2 = input("input number2: ")
# num3 = input("input number3: ")

# nums = [int(num1), int(num2), int(num3)]
# print(max(nums))

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
print (btc)