class Solution:
    def numTilings(self, n: int) -> int:

        MOD = 10**9 + 7
        memo = {0: 1, 1: 1, 2: 2}
        
        def f(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]

            else:
                memo[i] = (2*f(i-1)+f(i-3)) % MOD
                return memo[i]

        return f(n)
