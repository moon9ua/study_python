result = 0
nums = [4,1,2,1,2]
for num in nums:
    # result ^= num
    result = result ^ num 
    print (f"now: {result}")
print (f"result: {result}")