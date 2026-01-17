class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        safe = set()
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        def rec(r,c):

            for dr,dc in dir:
                nr,nc = r+dr,c+dc
                if (nr,nc) not in safe and 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == "O":
                    safe.add((nr,nc))
                    rec(nr,nc)
            
        a = len(board[0])-1
        b = len(board) - 1
        for i in range(len(board)):
            if board[i][0] == "O" and (i,0) not in safe:
                safe.add((i,0))
                rec(i,0)
            if board[i][a] == "O" and (i,a) not in safe:
                safe.add((i,a))
                rec(i,a)
        
        for i in range(len(board[0])):
            if board[0][i] == "O" and (0,i) not in safe:
                safe.add((0,i))
                rec(0,i)
            
            if board[b][i] == "O" and (b,i) not in safe:
                safe.add((b,i))
                rec(b,i)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in safe and board[i][j] == "O":
                    board[i][j] = "X"
        

            