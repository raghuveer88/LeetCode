class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        uniques_keys = list(set(nums))
        default_val = 0
        result_dict = dict.fromkeys(uniques_keys,default_val)
        for i in nums:
            result_dict[i] += 1

        max_val = max(result_dict,key=result_dict.get) 

        return max_val