class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        # This problem we can solve using BSF so each time you go to a point add all the possible next
        # steps which is up,down,left and right to the queue and now check from those points 
        #  if you are the last row or last col then you can simply exist and return the steps
        #  if you are not then just pop and move to next steps like a repetative process

        steps = 0
        q = deque([(entrance[0],entrance[1],steps)])
        possible_moves = [(-1,0),(1,0),(0,1),(0,-1)]

        visited = set()
        visited.add((entrance[0], entrance[1]))
        while q:
            x,y,steps = q.popleft()
            if (x == len(maze)-1 or y == len(maze[0])-1 or x == 0 or y == 0) and [x, y] != entrance:
                return steps
            else:
                for i,j in possible_moves:
                    if 0<= i+x < len(maze) and 0<= j+y < len(maze[0]) and maze[i+x][j+y] == '.' and (i+x,j+y) not in visited:
                        q.append((i+x,j+y,steps+1))
                        visited.add((i+x,j+y))
        return -1