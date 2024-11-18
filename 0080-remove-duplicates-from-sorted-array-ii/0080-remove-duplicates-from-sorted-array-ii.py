class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #it is all in the cpunt variable understand how you are counting and solve the problem
        j = 1
        count = 0

        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                count = count + 1
            else:
                count = 0

            if count < 2:
                nums[j] = nums[i]
                j = j +1
        return j