class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # THe operation XOR does is that a^a is zero so if the values are same then it is
        # zero. There for if we observe in the solution every terms will cancel out with 
        # other For example (0,0,1) is same as (1,1,0) only what will be left out is 
        # same sequence like (0,0,0) or (1,1,1) and so on
        res = nums[0]
        i = 1
        while i<len(nums):
            res = res^nums[i]
            i = i + 1

        return res