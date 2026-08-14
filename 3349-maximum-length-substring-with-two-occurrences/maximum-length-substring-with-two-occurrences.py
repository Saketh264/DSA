class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxi=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub=s[i:j+1]
                c=Counter(sub)
                if max(c.values())<=2:
                    maxi=max(maxi,len(sub))
        return maxi