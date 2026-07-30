class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        c,d=0,1
        while n>0:
            t=min(8,n)
            c+=(t*d)
            n-=8
            d+=1
        return c


        

        