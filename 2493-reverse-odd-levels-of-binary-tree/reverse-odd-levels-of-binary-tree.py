# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        level=0
        q=deque([root])
        while q:
            op=[]
            for i in range(len(q)):
                node=q.popleft()
                op.append(node)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if level%2!=0:
                l,r=0,len(op)-1
                while l<r:
                    op[l].val,op[r].val=op[r].val,op[l].val
                    l+=1
                    r-=1
            level+=1
        return root

