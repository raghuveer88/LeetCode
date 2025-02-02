class Solution:
    def rob(self, nums: List[int]) -> int:
    # for this problem just First create an array to store how much can you rob until a 
    # certain point then for every new value in the nums array check if the last robbed value
    # is more or the sum of the current house 'i' and the robbed house of i-2 is great
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0],nums[1])]

        i = 2
        while i < len(nums):
            dp.append(max(dp[i-1],nums[i]+ dp[i-2]))
            i = i + 1
        return dp[-1]


