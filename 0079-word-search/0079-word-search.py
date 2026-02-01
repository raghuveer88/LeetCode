class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        def rec(r,c,input):
            if board[r][c] != word[input]:
                return False
            if input >= len(word)-1:
                return True
            
            visited.add((r,c))
            for dr,dc in dir:
                nr,nc = r+dr, c+dc
                if nr>=0 and nr <len(board) and nc>=0 and nc < len(board[0]) and (nr,nc) not in visited:

                    if board[nr][nc] == word[input+1]:
                        if rec(nr,nc,input+1):
                            visited.remove((r, c))
                            return True
            
            visited.remove((r,c))
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if rec(i,j,0):
                    return True
        
        return False
