class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Approach:
        # 1. Find the maximum value in the `piles` array.
        #    This sets the upper bound for Koko's eating speed.
        #    The minimum speed is 1, and the maximum is the largest pile.
        # 2. Use binary search on the range (1, max(piles)) to find the smallest speed (K)
        #    that allows Koko to eat all the bananas within `h` hours.
        # 3. For each candidate speed `mid`, calculate the total time (`time_est`) needed 
        #    to eat all bananas. The time for each pile is `math.ceil(bananas / mid)`.
        # 4. If `time_est` > `h`, `mid` is too slow. Search the right half of the range.
        # 5. If `time_est` <= `h`, `mid` might be valid. Search the left half to find the minimum speed.
        # 6. The binary search will find the smallest valid eating speed.


        max_k = max(piles)
        

        l = 1
        r = max_k
        while l<=r:
            mid = (l+r) // 2
            time_est = 0
            for ban in piles:
                time_est += math.ceil(ban/mid)
            if time_est > h:
                l = mid +1
            elif time_est <= h:
                r = mid - 1
            
        return l