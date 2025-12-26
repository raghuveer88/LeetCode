class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 1
        prev = 0
        i = 1

        while i < len(nums):
            if nums[prev] == nums[i]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[prev+1] = nums[i]
                i += 1
                prev += 1

            if count >2:
                i = i+1
        
        return prev+1
            
        