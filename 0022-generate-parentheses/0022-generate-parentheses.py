class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def rec(open,closed,path):
            if len(path) == 2*n:
                res.append("".join(path[:]))
                return
            
            if open < n:
                path.append("(")
                rec(open+1,closed,path)
                path.pop()
            
            if closed < open:
                path.append(")")
                rec(open,closed+1,path)
                path.pop()
        
        rec(0,0,[])
        return res

                



                