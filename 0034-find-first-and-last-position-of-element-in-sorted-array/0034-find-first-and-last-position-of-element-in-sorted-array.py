class Solution:
    # this is a staight forward answer just peroform binary search you'll reach the answer

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.first(nums, target),self.second(nums, target)]
    def first(self, nums, target):
        low = 0
        high = len(nums)-1
        first = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return first

    def second(self, nums, target):
        low = 0
        high = len(nums)-1
        last = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            
            elif nums[mid] < target:
                low = mid + 1
            else:
                
                high = mid -1

        return last