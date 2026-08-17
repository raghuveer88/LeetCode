class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m, n = len(s), len(p)

        # dp[i][j] = whether s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Empty string vs pattern like a*, a*b*, a*b*c*
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        def matches(i: int, j: int) -> bool:
            """
            Return True if s[i - 1] matches p[j - 1] where p[j - 1] is not '*'.
            """
            return p[j - 1] == '.' or s[i - 1] == p[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    if matches(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Case 1: '*' means zero occurrences of the previous element
                    dp[i][j] = dp[i][j - 2]

                    # Case 2: '*' means one or more occurrences, if preceding char matches
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]