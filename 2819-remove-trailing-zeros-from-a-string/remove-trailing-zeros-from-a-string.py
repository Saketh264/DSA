class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ans=""
        for i in range(len(num)-1,-1,-1):
            if num[i]=='0':continue
            else: ans=num[:i+1]
            return ans
