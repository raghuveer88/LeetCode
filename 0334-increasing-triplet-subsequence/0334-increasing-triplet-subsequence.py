class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for i in range(len(nums)):
        #     if i == 0:
        #         pass
        #     elif nums[i-1] < nums[i] <nums[i+1]:
        #         return True
            
        # return False

        small = float('inf')
        med = float('inf')
        lar = float('inf')

        if len(nums)< 3:
            return False

        for i in nums:
            if i < small:
                small = i
            elif i < med and i > small:
                med = i
            elif i > med:
                lar = i
                return True

        return False
