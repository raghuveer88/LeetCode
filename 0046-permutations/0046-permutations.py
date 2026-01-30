class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        used = [False]*len(nums)
        def rec(path,used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                rec(path,used)
                path.pop()
                used[i] = False

        rec([],used)
        return res