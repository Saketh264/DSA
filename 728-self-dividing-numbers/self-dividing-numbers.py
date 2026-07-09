class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        op=[]
        for i in range(left,right+1):
            num=i
            while num>0:
                rem=num%10
                if rem ==0 or i%rem!=0: break
                num//=10
            if num==0:
                op.append(i)
        return op

        