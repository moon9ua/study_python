# 091
inventory = {
    "메로나" : [300, 20],
    "비비빅" : [400, 3],
    "죠스바" : [250, 100]
}
print (inventory)

# 092
print (inventory["메로나"][0], "원")

# 093
print (inventory["메로나"][1], "개")

# 094
inventory["월드콘"] = [500, 7]
print (inventory)

# 095
ice = list(inventory.keys())
print (ice)

# 097
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# price = list(icecream.values())
# print (sum(price))
print (sum(icecream.values()))

# 098
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print (icecream)

# 099
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print (result)

# 100
# 099와 마찬가지로 두 튜플도 zip을 통해 dict로 만들 수.