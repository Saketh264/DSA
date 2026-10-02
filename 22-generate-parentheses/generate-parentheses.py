class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        op=[]
        def backtrack(open,close,strs):
            if open==n and close==n: op.append(strs)
            if open!=n: backtrack(open+1,close,strs+"(")
            if close<open: backtrack(open,close+1,strs+")")
        backtrack(0,0,"")
        return op
