class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def rec(a,b):
            if b ==0:
                return 1
            if b == 1:
                return a
            if b == -1:
                return 1/a
            if b%2 != 0:
                half = rec(a,b//2)
                res = a*half*half
                return res
            else:
                half = rec(a,b//2)
                res = half*half
                return res

        return rec(x,n)