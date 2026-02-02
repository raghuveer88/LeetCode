"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        

        def validate(r,c,size):
            first = grid[r][c]
            for i in range(r,r+size):
                for j in range(c,c+size):
                    if grid[i][j] != first:
                        return False, first
            return True, first

        def solve(r,c,size):
            check,val = validate(r,c,size)
            if check:
                return Node(val,True,None,None,None,None)
            
            half = size//2
            tl = solve(r,c,half)
            tr = solve(r,c+half,half)
            bl = solve(r+half,c,half)
            br = solve(r+half,c+half,half)

            return Node(True,False,tl,tr,bl,br)

        
        return solve(0,0,len(grid))
            


                        
        