class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        count = 0
        nums.sort()

        while i < j:
            sum = nums[i] + nums[j]
            if sum < k:
                i = i+1
            elif sum > k:
                j = j-1
            else:
                count += 1
                i += 1
                j -= 1
    
        return count


        
        