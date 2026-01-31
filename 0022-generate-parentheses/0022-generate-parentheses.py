class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def rec(open,closed,path):
            if len(path) == 2*n:
                res.append(path)
                return
            
            if open < n:
                # path += "("
                rec(open+1,closed,path+"(")
                
            
            if closed < open:
                # path += ")"
                rec(open,closed+1,path+")")
                
        
        rec(0,0,"")
        return res

                



                