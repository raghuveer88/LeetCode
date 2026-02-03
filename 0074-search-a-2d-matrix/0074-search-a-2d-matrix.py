class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        targetRow = []
        for row in matrix:
            if row[-1] >= target:
                targetRow = row
                break
            
        
        def bst(l,r):

            if l > r:
                return False

            mid = (l+r)//2

            if targetRow[mid] == target:
                return True
            
            elif targetRow[mid] > target:
                return bst(l,mid-1)
            
            elif targetRow[mid] < target:
                return bst(mid+1,r)
            
        
        return bst(0,len(targetRow)-1)