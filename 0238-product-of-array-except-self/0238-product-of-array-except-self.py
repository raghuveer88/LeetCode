class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [nums[0]]
        right = list(reversed(nums))
        ans = []

        for i in range(1,len(nums)):
            left.append(left[i-1]*nums[i])

        for i in range(1,len(right)):
            right[i] = right[i-1]*right[i]

        right.reverse()

        for i in range(len(left)):
            if i-1 >=0 and i+1<len(left):
                ans.append(left[i-1]*right[i+1])
            elif i-1<0:
                ans.append(right[i+1])
            elif i+1 >= len(left):
                ans.append(left[i-1])

        return ans

# 1,2,6,12

# 24,24,12,4        
        