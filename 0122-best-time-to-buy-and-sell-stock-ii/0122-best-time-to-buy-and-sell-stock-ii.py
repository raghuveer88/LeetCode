class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash = 0
        hold = cash-prices[0]

        for p in prices:
            cash = max(cash,hold+p)
            hold = max(hold,cash-p)

        return cash