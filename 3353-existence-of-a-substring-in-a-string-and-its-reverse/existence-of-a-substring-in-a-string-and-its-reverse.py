class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        x=s[::-1]
        for i in range(len(s)-1):
            # print(s[i:i+2])
            if s[i:i+2] in x: 
                return True
        return False