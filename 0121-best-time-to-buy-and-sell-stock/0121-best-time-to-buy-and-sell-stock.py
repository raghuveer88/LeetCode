class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this uses a sliding window technique I took two pointers l and r then if the price of
        # l is less than r then update l to r. the goal is to find the a sum or difference which 
        #is greater than any pair we saw before.
        total = 0
        l = 0
        for r in range(1,len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                sum = prices[r] - prices[l]
                if sum > total:
                    total = sum
                    
                
        return total
