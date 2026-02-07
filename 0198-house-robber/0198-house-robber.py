class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def rec(i):
            if i in dp:
                return dp[i]
            if i >=len(nums):
                return 0
            dp[i] = max(rec(i+1),nums[i]+rec(i+2))
            return dp[i]

        return rec(0)
