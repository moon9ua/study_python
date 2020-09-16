import heapq

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print (sorted(nums, reverse=True))
print (sorted(nums, reverse=True)[k - 1])
print ()

print (heapq.nlargest(k, nums))