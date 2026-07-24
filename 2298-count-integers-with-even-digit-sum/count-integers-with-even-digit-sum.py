class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            k=i
            sums=0
            while k>0:
                rem=k%10
                sums+=rem
                k//=10
            if sums%2==0:c+=1
        return c
