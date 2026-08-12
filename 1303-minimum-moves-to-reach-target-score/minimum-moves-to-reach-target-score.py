class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        c=0
        while target>1:
            if target%2!=0:
                target-=1
                c+=1
            if maxDoubles>0:
                target//=2
                maxDoubles-=1
                c+=1
            else:
                return target+c-1
        return c