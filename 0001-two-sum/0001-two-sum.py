class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # For this use hash map first check the difference between the target and the 
        # element then check if the differece number is in the map. If not just add the 
        # element and it's index to the map.
        map = {}
        i = 0
        while i< len(nums):
            dif = target - nums[i]
            if dif in map:
                return [map[dif], i]
            map[nums[i]] = i
            i = i + 1
        
