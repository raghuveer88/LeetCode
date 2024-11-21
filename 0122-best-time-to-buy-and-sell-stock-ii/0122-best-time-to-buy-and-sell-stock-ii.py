class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # so firstly you can see this like a graph of prices. what we need to findout is everytime
        # there is a up from the down you add it to the final sum. at the end return the sum.
        l = 0
        sum = 0
        for r in range(1,len(prices)):
            if prices[l] > prices[r]:
                l = l+1
            else:
                sum = sum + prices[r] - prices[l]
                l = l+1
        
        return sum
            