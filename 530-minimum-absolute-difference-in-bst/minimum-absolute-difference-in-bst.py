# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root: return
        q=deque([root])
        op=[]
        while q:
            for i in range(len(q)):
                node=q.popleft()
                op.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        op.sort()
        mini=float('inf')
        for i in range(len(op)-1):
            mini=min(mini,op[i+1]-op[i])
        return mini

