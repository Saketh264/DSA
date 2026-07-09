class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        op=[]
        for i in range(left,right+1):
            s=str(i)
            valid=True
            for j in s:
                if int(j)==0 or i%int(j)!=0:
                    valid=False
            if valid:
                op.append(i)
        return op

        