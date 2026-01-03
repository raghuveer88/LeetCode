class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        direction = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
        dup = [row[:] for row in board]
        alive = 0

        for i in range(len(board)):
            for j in range(len(board[0])):

                for r,c in direction:
                    nr,nc = i + r, j+c
                    if 0<=nr<len(board) and 0<=nc<len(board[0]):
                        if dup[nr][nc] == 1:
                            alive += 1
                        # if board[nr][nc] == 0:
                        #     select["dead"] += 1
                if dup[i][j] == 1:
                    if alive < 2:
                        board[i][j] = 0
                    elif alive == 2 or alive == 3:
                        board[i][j] = 1
                    elif alive > 2:
                        board[i][j] = 0
                
                elif dup[i][j] == 0:
                    if alive ==3:
                        board[i][j] = 1
                
                alive = 0
            
