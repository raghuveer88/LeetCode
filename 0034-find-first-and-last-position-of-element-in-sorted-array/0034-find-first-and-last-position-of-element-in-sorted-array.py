class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        


        def bst(l,r,leftbias):
            
            i = -1
            while l <= r:
                
                mid = (l+r)//2

                if nums[mid] > target:
                    r = mid-1
                elif nums[mid] < target:
                    l = mid+1
                
                else:
                    i = mid
                    if leftbias:
                        r = mid-1
                    else:
                        l = mid+1
            
            return i
        
        a = bst(0,len(nums)-1,True)
        b = bst(0,len(nums)-1,False)

        return [a,b]
                        
