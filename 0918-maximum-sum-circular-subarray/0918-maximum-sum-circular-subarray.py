class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        current = 0
        best = float('-inf')
        
        total = 0
            


        mincurr = 0
        minbest = float('inf')
        maxcurr = 0
        maxbest = float('-inf')
        for i in range(len(nums)):
            mincurr = min(nums[i],mincurr+nums[i])
            minbest = min(minbest,mincurr)

            maxcurr = max(nums[i],maxcurr+nums[i])
            maxbest = max(maxbest,maxcurr)

            total = total+nums[i]



        if maxbest < 0:
            return maxbest
        
        return max(maxbest,total - minbest)

        

        