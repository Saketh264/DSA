class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m=len(board),len(board[0])
        path=set()
        def dfs(rows,cols,ind):
            if ind==len(word):
                return True
            if rows<0 or cols<0 or rows>=n or cols>=m or word[ind]!=board[rows][cols] or (rows,cols) in path:
                return False
            path.add((rows,cols))
            res=(dfs(rows+1,cols,ind+1) or dfs(rows-1,cols,ind+1) or dfs(rows,cols+1,ind+1) or dfs(rows,cols-1,ind+1))
            path.remove((rows,cols))
            return res
        for r in range(n):
            for c in range(m):
                if dfs(r,c,0): return True
        return False