class Solution:
    def rotate(self, nums: List[int], k: int) -> None:


        # just try to reverse the array according to the k values and concatinate the slices with reversing
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        # # nums = nums[::-1]
        # nums = nums[n-k:] + nums[:n-k] # this is one way to solve but the problem is it is won't change
        #nums directly as it is not in-place the below approach will work.
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]        