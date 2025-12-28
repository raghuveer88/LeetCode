class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        hash = set()


        for k in range(len(nums)-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k+1
            j = len(nums)-1
            target = -nums[k]
            while i<j:
                
                if nums[i] + nums[j] == target:
                    ans.append([nums[i],nums[j],nums[k]])
                    i =i+1
                    j = j-1
                    while i<j and nums[i] ==nums[i-1]:
                        i = i+1
                    while i<j and nums[j] ==nums[j+1]:
                        j = j-1
                elif nums[i] + nums[j] > target:
                    j = j-1
                elif nums[i] + nums[j] < target:
                    i = i+1

                
        
        return ans



        

