class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        maxi=0
        for i in s:
            if i=='(': 
                c+=1
                maxi=max(maxi,c)
            elif i==')': c-=1
        return maxi