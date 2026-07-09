class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums=0
        n=len(mat)
        m=len(mat[0])
        for i in range(n):
            for j in range(m):
                if i==j or i+j==n-1:
                    sums+=mat[i][j]
        return sums