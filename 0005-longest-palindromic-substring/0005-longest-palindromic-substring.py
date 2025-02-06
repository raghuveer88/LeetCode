class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        def expand(l, r):
            nonlocal res, res_len  # Use nonlocal since these are from the outer function
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:  # Check if this palindrome is the longest found
                    res = s[l: r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # Odd-length palindromes (centered at i)
            expand(i, i)

            # Even-length palindromes (centered between i and i+1)
            expand(i, i + 1)

        return res
