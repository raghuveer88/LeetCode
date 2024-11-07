class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # nums.insert(0,float('-inf''))
        # nums.append(float('-inf'))
        # a little truicky question need to tweak binary search a little. So to solve this problem
        # we know that the ends left most and right most are -inf (smallest) so we 
        # need to find which side the values is increaseing from the mid and move in that 
        # direction (that side of the array) so that at some point it will reduce for sure 
        # cuz the last indexes at the end values are smallest

        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = (l+r)//2
            if mid>0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            elif mid < len(nums)-1 and nums[mid+1] > nums[mid]:
                l = mid+1

            else:
                return mid

        
    