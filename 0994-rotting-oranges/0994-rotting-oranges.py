class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # In this problem firstly calculate the number of fresh organges
        # and append all the rotten oranges in the queue
        # and the 4 directions positions are mentioned in the possible_moves which is 
        # up, down, left and right. Now just do the 4 operation for all the rotten oranges
        # in the queue and as soon a fresh_orange is turned rotten reduce the fresh orange count
        # once all the fresh oranges are 0 then return the minutes else return -1
        q = deque()
        fresh_oranges = 0
        minutes = 0
        zero_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i,j,minutes))
                if grid[i][j] == 1:
                    fresh_oranges += 1
                

        possible_moves = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x,y, minutes = q.popleft()
            for i,j in possible_moves:
                if 0<=i+x<len(grid) and 0<=j+y<len(grid[0]) and grid[i+x][j+y] == 1:
                    grid[i+x][j+y] = 2
                    q.append((i+x,j+y,minutes+1))
                    fresh_oranges -= 1
        if fresh_oranges == 0:
                return minutes
        else:
            return -1
        
        