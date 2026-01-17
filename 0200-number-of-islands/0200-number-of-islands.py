class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        count = 0
        def rec(r,c):

            for dr,dc in dir:
                nr,nc = r+dr, c+dc
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr,nc) not in visited and grid[nr][nc] == "1":
                    visited.add((nr,nc))
                    rec(nr,nc)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]=="1":
                    visited.add((i,j))
                    count = count+1
                    rec(i,j)
        
        return count

                

