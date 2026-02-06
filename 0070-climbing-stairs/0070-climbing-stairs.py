class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo= {}
        def rec(n):
            if n in memo:
                return memo[n]
            if n ==0 or n ==1:
                return 1
            memo[n] = rec(n-1) + rec(n-2)
            return memo[n]
        
        return rec(n)