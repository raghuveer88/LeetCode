class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # k = 0
        # for i in range(len(nums)):
        #     if i -1 >= 0:
        #         if nums[i-1] > nums[i]:
        #             k = i
        #             nums = nums[k:] + nums[0:k]
        #             break


        def bst(l,r):
            if l >r:
                return -1
            
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                
                if nums[l] <=target< nums[mid]: 
                    return bst(l,mid-1)
                else:
                    return bst(mid+1,r)
            else:
                if nums[mid] < target <= nums[r]:
                    return bst(mid+1,r)
                else:
                    return bst(l,mid-1)


            
            
        return bst(0,len(nums)-1)
