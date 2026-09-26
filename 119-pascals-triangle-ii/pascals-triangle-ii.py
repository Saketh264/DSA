class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        op=[]
        for i in range(rowIndex+1):
            val=[1]*(i+1)
            for j in range(1,i):
                val[j]=op[i-1][j-1]+op[i-1][j]
            if i==rowIndex: return val
            op.append(val)