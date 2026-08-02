class Solution:
    def minOperations(self, n: int) -> int:
        sums=0
        got=[]
        for i in range(n):
            sums=(2*i)+1
            got.append(sums)
        target=sum(got)//n
        og=[target]*n
        tot=0
        for i in range(len(og)):
            tot+=abs(got[i]-og[i])
        return tot//2
        