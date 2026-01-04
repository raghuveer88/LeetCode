class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        res = []
        i = 0
        j = 0
        
        while i < len(nums):
            if j+1 < len(nums) and nums[j+1] == nums[j]+1:
                j = j+1
                continue
            if j-i > 0:
                res.append(str(nums[i])+"->"+str(nums[j]))
            if j-i == 0:
                res.append(str(nums[i]))
            i = j+1
            j = i
        return res


            
            
                
            