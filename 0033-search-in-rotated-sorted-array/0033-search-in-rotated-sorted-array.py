class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        k = 0
        for i in range(len(nums)):
            if i -1 >= 0:
                if nums[i-1] > nums[i]:
                    k = i
                    nums = nums[k:] + nums[0:k]
                    break


        


        def bst(l,r):
            if l >r:
                return -1
            
            mid = (l+r)//2

            if nums[mid] == target:
                return (mid + k)% len(nums)
            
            elif nums[mid] > target:
                return bst(l,mid-1)
            elif nums[mid] < target:
                return bst(mid+1,r)
            
        return bst(0,len(nums)-1)
