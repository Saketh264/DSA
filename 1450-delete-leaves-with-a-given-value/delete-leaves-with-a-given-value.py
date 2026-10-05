# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
        op=[]
        def backtrack(node):
            if not node: return None
            node.left=backtrack(node.left)
            node.right=backtrack(node.right)
            if not node.left and not node.right and node.val==target: return None
            return node
        return backtrack(root)

