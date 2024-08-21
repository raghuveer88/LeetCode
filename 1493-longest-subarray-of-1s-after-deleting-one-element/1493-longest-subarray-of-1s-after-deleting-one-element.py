class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #similar to the previous problem have a window size of 
        # L and R then increment L if zeros are more than 1
        # calculate the width and return the max width
        l = 0
        r = 0
        width = 0
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            w = i - l 
            width = max(width,w)

        return width