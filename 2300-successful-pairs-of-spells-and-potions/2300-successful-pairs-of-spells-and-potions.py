class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        n = len(spells)
        m = len(potions)
        potions.sort()
        for i in range(n):
            count = 0
            temp = 0
            low, high = 0, m-1
            while low <= high:
                mid = (low + high)//2
                if spells[i]*potions[mid]>= success:
                    high = mid -1
                    temp = mid
                    count = m -temp
                else:
                    low = mid+1
                
            ans.append(count)

        return ans
            