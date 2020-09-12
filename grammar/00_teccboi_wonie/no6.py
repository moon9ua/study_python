## https://youtu.be/_CY4DlRCTBc
## 자료구조(리스트, 튜플, 딕셔너리)


## <리스트>
# x = list()
# y = []
# print(x); print(y)

# x = [1,2,3]
# y = ['hi', 'hello']
# z = ['hi', 1, 2, 3]
# print(x + y)
# print(x[0])
# x[2] = 10; print(x)

# x = [4, 2, 3, 1]
# num_elements = len(x)
# print(num_elements)

# y = sorted(x); print(y)
# z = sum(x); print(z)

# for n in x:
# 	print(n)

# y = ["hello", "world"]
# for c in y:
# 	print(c)

# x = [4, 2, 3, 1]
# y = ["hello", "world"]
# print(x.index(3))
# print(y.index("hello"))
# # print(x.index(6))		# 없으면 에러뜸.
# print("hello" in y)
# print("bye" in y)
# if "hello" in y:
# 	print("hello가 있어요")


## <튜플>
# x = tuple()
# y = ()

# x = (1,2,3)
# y = ('a', 'b', 'c')
# z = (1, 'hello', 'world')
# print(x+y)
# print('a' in y)
# print(z.index(1))
## x[0] = 10		# 에러남.
## 튜플은 assignment가 안됨. 튜플은 immutable. 리스트는 mutable.


## <딕셔너리>
# x = dict()
# y = {}

# x = {
# 	"name": "워니",
# 	"age": 20,
# }
# print(x)
# print(x["name"])
# print(x["age"])

# x = {
# 	0: "wonie",
# 	1: "hello",
# 	"age": 20,
# }

# print(x[0])
# print(x[1])
# print(x["age"])

# print("age" in x)
# print("name" in x)

# print(x.keys())
# print(x.values())

# for key in x:
# 	print("key: " + str(key))
# 	print("values: " + str(x[key]))

# x[0] = "워니"; print(x)
# x["school"] = "한빛"; print(x)


## <복습코딩>
## 과일의 수를 세는 프로그램
fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

d = {}

for f in fruit:
	if f in d:
		d[f] = d[f] + 1
	else:
		d[f] = 1

print(d)