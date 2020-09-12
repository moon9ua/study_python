# 171
# price_list = [32100, 32150, 32000, 32500]
# # for i in range(4):
# for i in range(len(price_list)): # 더 좋은 코드
#     print(price_list[i])

# 172
# price_list = [32100, 32150, 32000, 32500]
# for i, data in enumerate(price_list): # enumerate()
#     print(i, data)

# 175
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) - 1):
    # print(my_list[i], my_list[i + 1])

# 177
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) - 1, 0, -1):
#     print (my_list[i], my_list[i - 1])

# 178
my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1):
    print (my_list[i + 1] - my_list[i])
