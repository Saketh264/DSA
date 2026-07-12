# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        op=[]
        stack=[]
        def dfs(node):
            if not node:
                return 
            stack.append(str(node.val))
            if not node.left and not node.right:
                op.append(int(''.join(stack.copy())))
            dfs(node.left)
            dfs(node.right)
            stack.pop()
        dfs(root)
        return sum(op)