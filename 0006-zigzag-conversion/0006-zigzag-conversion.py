class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""]*numRows

        go_down = True
        r = 0

        for c in s:
            
            rows[r] += c
            if r == 0:
                go_down = True
            if r == numRows-1:
                go_down = False
            if go_down:
                r = r+1
            else:
                r = r-1
        
        return "".join(rows)
            
                





        

