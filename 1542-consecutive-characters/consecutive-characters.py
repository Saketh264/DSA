class Solution:
    def maxPower(self, s: str) -> int:
        c=1
        maxi=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:c+=1
            else: 
                maxi=max(maxi,c)
                c=1
        return max(maxi,c)
        