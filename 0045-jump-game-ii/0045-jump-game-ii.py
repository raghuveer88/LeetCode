class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        farest_idx = 0
        present_idx = 0
        n = len(nums) - 1
        for i in range(len(nums)-1):
            farest_idx = max(farest_idx, i+nums[i])

            if i == present_idx:
                count += 1
                present_idx = farest_idx
                if present_idx >= n:
                    break

            
        return count