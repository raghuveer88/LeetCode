class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # quite simple you just need to sort potions and do bnary search to get the elment 
        # which is the first element when multiplied with spell is greater than success
        # so all the other elements to the right will automatically be greater 
        
        potions = sorted(potions)
        count = []
        
        for i in spells:
            l,r = 0,len(potions)-1
            idx_val = len(potions)
            while l <= r:
                m = (l + r) //2
                if i * potions[m] >= success:
                    r = m -1
                    idx_val = m
                else:
                    l = m +1
            count.append(len(potions) - idx_val)

        return count