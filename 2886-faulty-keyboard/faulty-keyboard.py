class Solution:
    def finalString(self, s: str) -> str:
        strs=""
        for i in s:
            if i=='i':
                strs=strs[::-1]
            else: strs+=i
        return strs