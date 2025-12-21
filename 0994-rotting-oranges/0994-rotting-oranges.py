class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        minutes = -1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:

            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr,c+dc

                    if nr >=0 and nr < rows and nc >=0 and nc < cols:
                        if grid[nr][nc] == 1:
                            fresh -= 1
                            grid[nr][nc] = 2
                            q.append((nr,nc))
            
            minutes += 1

        
        if fresh == 0:
            return minutes
        else:
            return -1
                    
