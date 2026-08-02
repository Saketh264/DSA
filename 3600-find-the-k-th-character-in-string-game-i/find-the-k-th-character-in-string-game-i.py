class Solution:
    def kthCharacter(self, k: int) -> str:
        strs='a'
        while len(strs)<=k:
            for i in range(len(strs)):
                strs+=chr(ord(strs[i])+1)
        return strs[k-1]
