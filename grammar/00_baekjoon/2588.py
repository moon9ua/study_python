a = int(input())
b = int(input())

# a = 472
# b = 385

print(a * ((b%100)%10))
print(a * ((b%100)//10))
print(a * (b//100))
print(a*b)