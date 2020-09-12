# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ret = 0 # 다른 방법 없나? -> 392p에 나와있음.
    # 중첩 함수에서 클래스 변수를 사용한 이유:
    # 대충 불변 객체라 재할당돼서 그렇다는 내용...
    # 불변 객체이므로, 재할당하면 id가 변경돼서 '로컬 변수'로 바뀐다고 함.
    # 리스트나 딕셔너리는 append()를 통해 재할당 없이 변경 가능해서 함수 내의 변수로 해도 된다고.
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.ret = max(self.ret, left + right + 2) # 거리 갱신 # self를 안 붙이면 오류가 뜸.
            return max(left, right) + 1 # 상태값

        dfs(root)
        return self.ret

a = 12
print (id(a))
a = 23
print (id(a))
