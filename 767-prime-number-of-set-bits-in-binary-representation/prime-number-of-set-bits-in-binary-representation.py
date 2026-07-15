class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c=0
        for i in range(left,right+1):
            x=bin(i).count('1')
            prime=True
            if x>=2:
                for i in range(2,int(math.sqrt(x))+1):
                    if x%i==0:
                        prime=False
                        break
                if prime:
                    c+=1
        return c