class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digittostr = {
            "2" : "abc",
            '3' : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtracking(i, currstr):
            if len(currstr) == len(digits):
                res.append(currstr)
                return 
            for c in digittostr[digits[i]]:
                backtracking(i+1,currstr + c)

        if digits:
            backtracking(0,"")

        return res