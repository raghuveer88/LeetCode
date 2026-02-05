class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                i = i+3
            else:
                return nums[i-1]
        
        return nums[i-1]
            

        