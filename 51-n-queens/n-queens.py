class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        def safe(row,col):
            duprow=row
            dupcol=col
            while row>=0 and col>=0:
                if board[row][col]=='Q': return False
                row-=1
                col-=1
            row=duprow
            col=dupcol
            while col>=0:
                if board[row][col]=='Q': return False
                col-=1
            row=duprow
            col=dupcol
            while col>=0 and row<n:
                if board[row][col]=='Q': return False
                row+=1
                col-=1
            return True
        op=[]
        def solve(col):
            if col==n:
                op.append([''.join(row) for row in board])
                return 
            for i in range(len(board)):
                if safe(i,col):
                    board[i][col]='Q'
                    solve(col+1)
                    board[i][col]='.'
        solve(0)
        return op
