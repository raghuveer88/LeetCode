class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        lowest = prices[0]
        res = 0

        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            
            res = max(res,prices[i]-lowest)

        return res

            