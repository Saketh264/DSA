class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        c={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        ans=[]
        def comb(ind,stack):
            if ind==len(digits):
                ans.append(''.join(stack))
                return 
            for i in c[digits[ind]]:
                stack.append(i)
                comb(ind+1,stack)
                stack.pop()
        comb(0,[])
        return ans