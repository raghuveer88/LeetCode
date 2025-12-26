class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k=k%size
        for i in range(k):
            h = nums.pop()
            nums.insert(0,h)


