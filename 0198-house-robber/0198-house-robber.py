class Solution:
    def rob(self, nums: List[int]) -> int:
    # for this problem just First create an array to store how much can you rob until a 
    # certain point then for every new value in the nums array check if the last robbed value
    # is more or the sum of the current house 'i' and the robbed house of i-2 is great
        memo = {}
        n = len(nums)

        def rec(i):
            if i >=n:
                return 0

            if i in memo:
                return memo[i]

            else:
                memo[i] = max(nums[i]+ rec(i+2), rec(i+1))
                return memo[i]


        return rec(0)
