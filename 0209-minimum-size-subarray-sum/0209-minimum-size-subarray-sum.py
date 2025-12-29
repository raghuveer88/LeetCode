class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = float(inf)
        i = 0
        sum = 0

        for j in range(len(nums)):
            sum = sum + nums[j]

            while sum >= target:
                res = min(res,j-i+1)
                sum = sum - nums[i]
                i = i+1
        return 0 if res == float(inf) else res



        