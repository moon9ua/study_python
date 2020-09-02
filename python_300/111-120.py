# 111
# tmp = input() # input()
# print (tmp * 2)

# 112
# tmp = input("숫자를 입력하세요: ")
# print (int(tmp) + 10)

# 113
# tmp = int(input())
# if tmp % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# 116
# tmp = input("현재시간:")
# time = tmp.split(":")
# if time[1] == "00":
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다.")

# 117
# fruit = ["사과", "포도", "홍시"]
# tmp = input("좋아하는 과일은? ")
# if tmp in fruit: # in
#     print ("정답입니다.")
# else:
#     print ("정답ㄴㄴ")

# 119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# tmp = input("제가좋아하는계절은:")
# # if tmp in fruit.keys():
# if tmp in fruit:
#     print ("정답입니다.")
# else:
#     print("정답ㄴㄴ")

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
tmp = input("좋아하는과일은?")
if tmp in fruit.values():
    print("정답")
else:
    print("오답")