class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        path = []
        ans = []

        def backtrack(start,k_left,remain):
            if k_left == 0:
                if remain == 0:
                    ans.append(path[:])
                return
            if remain < 0:
                return

            for x in range(start,10):
                if x > remain:
                    break
                path.append(x)
                backtrack(x+1,k_left-1,remain-x)
                path.pop()

        backtrack(1,k,n)
        return ans