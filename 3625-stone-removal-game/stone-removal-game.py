class Solution:
    def canAliceWin(self, n: int) -> bool:
        val=10
        c=0
        while n-val>=0:
            n-=val
            val-=1
            c+=1
        return c%2!=0
