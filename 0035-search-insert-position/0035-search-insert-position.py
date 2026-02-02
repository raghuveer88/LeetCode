class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        def bst(l,r):

            if l > r:
                return l
            
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                return bst(l,mid-1)
            
            elif nums[mid] < target:
                return bst(mid+1,r)

        return bst(0,len(nums)-1)