class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        sol = []
        res = []

        def rec(sol,i):
            if len(sol) == k:
                res.append(sol[:])
                return

            for v in range(i,n+1):
                sol.append(v)
                rec(sol,v+1)
                sol.pop()
        
        rec([],1)
        return res