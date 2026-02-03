class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) ==1:
            return 0

        def bst(i):

            if i-1 >=0 and i + 1 < len(nums):
                if nums[i-1] < nums[i] > nums[i+1]:
                    return i
            
            elif i-1 < 0:
                if nums[i] > nums[i+1]:
                    return i
            
            elif i+1 >= len(nums):
                if nums[i-1] < nums[i]:
                    return i
            
            if i + 1 <= len(nums) and nums[i+1]>= nums[i]:
                return bst(i+1)
            elif i -1 >= 0 and nums[i-1] >= nums[i]:
                return bst(i-1)
        
        mid = (len(nums)-1)//2
        return bst(mid)
            


