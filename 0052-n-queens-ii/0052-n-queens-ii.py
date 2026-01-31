class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posdiagnal = set()
        negdiagnal = set()

        res = 0
        def rec(r):
            if r == n:
                nonlocal res
                res += 1
                return 
            
            for c in range(n):
                if c in col or (r+c) in posdiagnal or (r-c) in negdiagnal:
                    continue
                col.add(c)
                posdiagnal.add(r+c)
                negdiagnal.add(r-c)
                rec(r+1)
                col.remove(c)
                posdiagnal.remove(r+c)
                negdiagnal.remove(r-c)

        rec(0)
        return res
