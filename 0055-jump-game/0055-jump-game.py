class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal = len(nums)-1
        # j = 0

        # if goal == 0:
        #     return True

        # for i in range(len(nums)-1):
        #     j = i + nums[i]
        #     if j >= goal:
        #         return True

            
        
        # return False

        goal = len(nums)-1
        farest = 0
        i = 0

        while i<=farest:
            farest = max(farest,i+nums[i])

            if farest >= goal:
                return True
            i = i+1

        
        return False

