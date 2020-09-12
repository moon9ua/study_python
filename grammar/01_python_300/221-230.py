# 221
def print_reverse(str):
    print(str[::-1])
print_reverse("python")

# 223
def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)
print_even ([1, 3, 2, 10, 12, 11, 15])

# 224
def print_keys(dict):
    for i in dict.keys():
        print(i)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(dict, key):
    print(dict[key])
print_value_by_key  (my_dict, "10/26")

# 226
def print_5xn(str):
# 풀다가 말았음. 나중에 다시...