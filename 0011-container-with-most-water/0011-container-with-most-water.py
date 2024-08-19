class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        i = 0
        j = len(height) - 1
        ans = 0
        
        while j > i:
            ans = max(min(height[i],height[j])*(j-i),ans)
            if height[i] <= height[j]:
                i = i+1
            elif height[j] < height[i]:
                j = j-1
            
        
        return ans
