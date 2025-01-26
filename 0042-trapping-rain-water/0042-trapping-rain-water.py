class Solution:
    def trap(self, height: List[int]) -> int:
        # find the max of the left and max of right and which ever max is less try to 
        # traverse from that side and subtract each ith element with the max of its 
        # corresponding side. If the max of the traversing side is more than the other side
        # then start travesing from the other side until you find an other new max.
        l,r  = 0,len(height)-1
        maxLeft,maxRight = height[l],height[r]
        res = 0
        while l<r:
            if maxLeft < maxRight:
                l = l + 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r = r - 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]

        return res
