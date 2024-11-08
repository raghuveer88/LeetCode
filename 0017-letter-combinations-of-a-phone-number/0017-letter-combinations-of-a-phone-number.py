class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # It maps each digit (from '2' to '9') to its corresponding letters,
        #  then uses a recursive function to build combinations by exploring
        #  each letter option for the current digit. If a combination matches 
        # the length of the input digits, it’s added to the result list. 
        # The recursion continues until all possible combinations are 
        # explored, returning the list of results.
        
        
        res = []
        map_nums_digit = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backtracking(i,currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for c in map_nums_digit[digits[i]]:
                backtracking(i+1,currStr + c)

        
        if digits:
            backtracking(0,"")
        
        return res