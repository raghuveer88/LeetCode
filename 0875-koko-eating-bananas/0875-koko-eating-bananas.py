class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)

        mid = (low + high)//2

        estimate = sum(ceil(pile/mid) for pile in piles)

        while low<=high:
            mid = (low + high)//2

            estimate = sum(ceil(pile/mid) for pile in piles)
            if estimate > h:
                low = mid+1
            elif estimate <= h:
                high = mid-1


        return low
