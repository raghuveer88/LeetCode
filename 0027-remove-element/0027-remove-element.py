class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # In this problem we are solving it using two pointer. I think what I have noticed is 
        # when using two pointer approach you need to use while loop with a condition including
        # pointers and not the array size. so for this sum took a start point and the end point
        # if I see a nums[start] with a val just swap it to the end and decrement the end by 1 
        # but don't increament the start as the swapped end might still be a value with val so needs
        # to be checked again.


        end = len(nums) - 1
        start = 0

        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                nums[end] = val
                end = end -1

            else:
                start = start + 1

        return end+1

        
            