class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        rows = len(strs)
        deletion = 0
        for c in range(cols):
            for r in range(rows-1):
                if strs[r][c] > strs[r+1][c]:
                    deletion += 1
                    break
        
        return deletion

