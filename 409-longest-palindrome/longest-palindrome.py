class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        odd,tot=0,0
        for i in c:
            if c[i]%2==0:tot+=c[i]
            else:
                tot+=c[i]-1
                odd=1
        return tot+odd