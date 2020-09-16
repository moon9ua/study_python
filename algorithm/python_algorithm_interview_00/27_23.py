# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# import collections
from typing import List
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # root = result = ListNode(None)
        heap = []

        for lst in lists:
            heapq.heappush(heap, (lst.val, lst))

        # for i in range(len(lists)):
        #     if lists[i]:
        #         heapq.heappush(heap, (lists[i].val, i, lists[i]))

        print (heap)
        # while heap:
        #     node = heapq.heappop(heap)
        #     idx = node[1]
        #     result.next = node[2]

sol = Solution()
lists = [[1,4,5],[1,3,4],[2,6]]
print(type(lists[0]))
sol.mergeKLists(lists)