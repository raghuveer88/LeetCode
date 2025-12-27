class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        n = len(citations)
        # visited = set()
        
        for i,c in enumerate(citations):
            h = n-i
            if c>=h:
                return h    
        
        return 0
    
# 0,1,3,6,5