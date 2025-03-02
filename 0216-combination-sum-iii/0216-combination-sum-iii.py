class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dsf(curr,n,k,start):
            if n==0 and k == 0:
                res.append(curr)
                return
            if k <=0:
                return

            for i in range(start,min(n+1,10)):
                dsf(curr + [i], n-i, k-1,i + 1)
            return
        dsf([],n,k,1)

        return res