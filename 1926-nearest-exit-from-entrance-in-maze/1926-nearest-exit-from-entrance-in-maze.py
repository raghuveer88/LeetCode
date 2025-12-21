class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze),len(maze[0])
        sr,sc= entrance[0],entrance[1]
        step = 0
        q = deque([(sr,sc,step)])

        direction = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = set([(sr,sc)])

        while q:
            r,c,step = q.popleft()
            
            for dr,dc in direction:
                ur,uc = r+dr,c+dc
                if ur<0 or ur>=rows or uc<0 or uc>=cols:
                    continue
                if maze[ur][uc] != '.':
                    continue
                
                if (ur,uc) in visited:
                    continue

                if ur == rows-1 or ur == 0 or uc == cols-1 or uc == 0:
                    return step + 1
                visited.add((ur,uc))
                q.append((ur,uc,step+1))
                
        return -1



