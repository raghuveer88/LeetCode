class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cur_sum = sum(nums[0:k])
        ans = cur_sum
        avg = float(cur_sum)/float(k)
        

        for i in range(1,len(nums)-k+1):
            cur_sum = cur_sum - nums[i-1] + nums[i+k-1]
            ans = max(ans,cur_sum)
            
                
        return float(ans)/k