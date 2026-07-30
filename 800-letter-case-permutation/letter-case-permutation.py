class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        op=[]
        def dfs(i,path):
            if i==len(s):
                op.append(path)
                return
            if s[i].isdigit():dfs(i+1,path+s[i])
            else:
                dfs(i+1,path+s[i].lower())
                dfs(i+1,path+s[i].upper())
        dfs(0,"")
        return op

