class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        def bst(l,r):
            while l < r:

                mid = (l+r)//2

                if nums[mid] > nums[r]:
                    l = mid+1


                elif nums[mid] < nums[r]:
                    r = mid
                else:
                    r = r-1

                
            return nums[l]
     
            

        return bst(0,len(nums)-1)