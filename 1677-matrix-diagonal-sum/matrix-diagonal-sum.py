class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums=0
        n=len(mat)
        for i in range(n):
            sums+=mat[i][i]
            if i!=n-i-1:
                sums+=mat[i][n-i-1]
        return sums