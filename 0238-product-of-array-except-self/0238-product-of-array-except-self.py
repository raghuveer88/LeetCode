class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        right = 1
        for i in range(len(nums)):
            if i == 0:
                result.append(1)
            else:
                result.append(nums[i-1] * result[i-1])
        
        for i in range(len(nums),0,-1):
            if not i == len(nums):
                right = right * nums[i]
                result[i-1] = right * result[i-1]


        return result
