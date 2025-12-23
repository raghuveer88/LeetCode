class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def rec(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]

            else:
                memo[i] = min(rec(i-1)+cost[i-1],
                            rec(i-2)+cost[i-2])
                return memo[i]

        
        return rec(n)