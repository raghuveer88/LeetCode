class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        size = len(nums)
        if size==1:
            return nums
        i = 0
        j = 1
        while j<size:
            if j >= size:
                return nums
            elif nums[i] == 0 and nums[j] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i = i+1
                j = j+1
            elif nums[i] == 0 and nums[j] == 0:
                j = j+1
            else:
                i = i + 1
                j = j + 1