class Solution:
    def mySqrt(self, x: int) -> int:
        

        left = 0
        right = x
        ans = 0
        while left <= right:
            mid = (left+right)//2
            temp = mid**2
            if temp <= x:
                ans = mid
                left = mid+1
            elif temp > x:
                right =  mid-1
        
        return ans