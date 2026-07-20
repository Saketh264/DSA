class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        m,n=len(grid),len(grid[0])
        k%=(m*n)
        for i in grid:
            arr.extend(i)
        arr=arr[-k:]+arr[:-k] 
        grid1=[]
        for i in range(0,len(arr),n):
            grid1.append(arr[i:i+n])
        return grid1
        # m=len(grid)
        # n=len(grid[0])
        # for x in range(k):
        #     last=grid[m-1][n-1]
        #     for i in range(m-1,-1,-1):
        #         for j in range(n-1,-1,-1):
        #             if i==0 and j==0: grid[0][0]=last
        #             elif j==0: grid[i][0]=grid[i-1][n-1]
        #             else: grid[i][j]=grid[i][j-1]
        # return grid
            