class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        


        def bst(l,r):
            if l > r:
                return [-1,-1]

            if nums[l]== nums[r] == target:
                return [l,r]
            
            mid = (l+r)//2

            if nums[mid] > target:
                return bst(l,mid-1)
            if nums[mid] < target:
                return bst(mid+1,r)
            
            if nums[mid] == target:
                if nums[mid] != nums[r] and nums[mid] != nums[l]:
                    return bst(l-1,r-1)
                if nums[mid] != nums[r]:
                    return bst(l,r-1)
                if nums[mid] != nums[l]:
                    return bst(l+1,r)
        
        return bst(0,len(nums)-1)
            