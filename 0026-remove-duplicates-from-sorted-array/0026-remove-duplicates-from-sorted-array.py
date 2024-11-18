class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # since the array is already in acending order. evertime you enconter a new 
        # number for the first time asiign it to jth index which is responsiable to 
        #change have the unique elements from beginning.

        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1

        return j