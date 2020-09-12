import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue = collections.deque([root]) # deque. 리스트를 사용해도 되지만, 데크 자료형은 이중 연결리스트로 양방향 모두 O(1) 추출 가능하므로.
        depth = 0

        while queue: # bfs는 큐로. bfs는 재귀가 아닌 반복으로도 가능.
            depth += 1
            for _ in range(len(queue)): # 처음에 len(queue)를 구한 후 고정됨. 중간에 queue가 추가돼도 반복문에 영향 x.
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

        return depth