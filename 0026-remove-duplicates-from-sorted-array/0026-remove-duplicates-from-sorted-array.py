class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev = 0

        for i in range(len(nums)):
            if nums[prev] == nums[i]:
                continue
            else:
                nums[prev+1] = nums[i]
                prev += 1

        return prev+1        