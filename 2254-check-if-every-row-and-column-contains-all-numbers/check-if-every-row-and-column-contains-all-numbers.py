class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        target=set(range(1,n+1))
        for row in matrix:
            if set(row)!=target:
                return False
        for j in range(n):
            if {matrix[i][j] for i in range(n)}!=target:
                return False
        return True
