class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1
        leftmin =height[i]
        rightmin = height[j]
        res = 0
        while i < j:
            minimum = min(height[i],height[j])
            dist = j -i
            res = max(res,minimum*dist)
            if minimum == height[i]:
                i = i+1
            else:
                j = j -1

        
        return res
            



