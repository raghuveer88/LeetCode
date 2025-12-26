class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = 0
        count = 0

        for i in nums:
            if count == 0:
                res = i
            if i == res:
                count = count +1
            else:
                count = count -1

        
        return res