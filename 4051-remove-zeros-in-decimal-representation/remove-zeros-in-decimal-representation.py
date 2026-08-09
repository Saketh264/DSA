class Solution:
    def removeZeros(self, n: int) -> int:
        n=str(n)
        strs=""
        for i in n:
            if i!='0':
                strs+=i
        return int(strs)
        