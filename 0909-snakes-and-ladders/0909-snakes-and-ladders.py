class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        board.reverse()
        def helper(num):
            r = (num-1) // n
            c = (num-1) % n
            if r%2:
                c = n-1-c
            return [r,c]
        
        q = deque()
        q.append((1,0))
        visited = set()
        visited.add(1)
        while q:
            num,moves = q.popleft()
            for i in range(1,7):
                next_num = num+i
                r,c = helper(next_num)
                if board[r][c] != -1:
                    next_num = board[r][c]
                if next_num == n*n:
                    return moves+1
                if next_num not in visited:
                    q.append((next_num,moves+1))
                    visited.add(next_num)
        return -1
            
            
                
                
            