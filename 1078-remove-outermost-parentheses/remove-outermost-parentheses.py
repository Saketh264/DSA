class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        level=0
        res=[]
        for i in s:
            if i=='(': 
                level+=1
                if(level>1):
                    res.append(i)
            elif(i==')'):
                if(level>1):res.append(i)
                level-=1
        return ''.join(res)


