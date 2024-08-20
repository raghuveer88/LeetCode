class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #  so you'll need to adjust the window size while checking if 
        # the number of 0's exceded K value 

        window_size = 0
        left = 0
        num_zeros = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            w = r-left+1
            window_size = max(window_size,w)

        return window_size 