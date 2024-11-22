class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # first keep max_index to where the i+nums[i] can go max. so which means now unitl that
        #max_index you can access any element you want. By any chance if the for look index 'i'
        # is greater than max_index which means you are not able to access that index return false.
        max_index = 0
        for i in range(len(nums)):
            if i > max_index:
                return False
            else:
                temp = i + nums[i]
                max_index = max(max_index, temp)
            
        return True