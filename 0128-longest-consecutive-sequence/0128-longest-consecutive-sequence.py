class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        longest = 0

        for x in s:
            if x - 1 in s:
                continue
            y = x
            while y in s:
                y += 1
            longest = max(longest, y - x)

        return longest