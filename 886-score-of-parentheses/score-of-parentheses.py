class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        op=[0]
        for i in s:
            if i=='(': op.append(0)
            else:
                val=op.pop()
                if val==0: val=1
                else: val=2*val
                op[-1]+=val
        return op[-1]

