class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = ""
        for r in range(numRows):
            increment = (numRows-1)*2
            for j in range(r, len(s), increment):
                res += s[j]
                if (r>0 and r < numRows -1 and j+ increment - 2 * r <len(s)):
                    res += s[j + increment -2*r]
        return res