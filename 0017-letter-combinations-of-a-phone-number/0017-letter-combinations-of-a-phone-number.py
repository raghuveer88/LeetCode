class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapper = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        res = []
        path = []
        def rec(path,i):
            if len(path)== len(digits):
                res.append("".join(path[:]))
                return
            
            
            for v in mapper[digits[i]]:
                path.append(v)
                rec(path,i+1)
                path.pop()
        
        rec([],0)
        return res
