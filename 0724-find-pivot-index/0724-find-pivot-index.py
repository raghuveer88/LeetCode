class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # just calculate the total and substract the left sum of it (including the num[index])
        # the check if it's equal to left sum if yes return the index

        l = 0
        r = len(nums)-1
        sum_left = 0
        sum_right = 0
        total_sum = sum(nums)


        for i in range(len(nums)):        
            sum_right = total_sum - sum_left - nums[i]
            if sum_left == sum_right:
                return i
            sum_left = sum_left + nums[i]
        return -1
            



        