from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2 # 몫

        node = TreeNode(nums[mid])
        print (id(nums))
        node.left = self.sortedArrayToBST(nums[:mid]) # 복사된 배열?
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node