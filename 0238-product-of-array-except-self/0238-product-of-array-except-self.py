class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize prefix and suffix arrays
        pre = [1] * n
        suf = [1] * n
        
        # Compute prefix product
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        # Compute suffix product
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        
        # Compute result using prefix and suffix
        res = []
        for i in range(n):
            res.append(pre[i] * suf[i])
        
        return res
