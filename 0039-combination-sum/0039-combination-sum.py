class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []


        def rec(path,ind):
            if sum(path) == target:
                res.append(path[:])
                return
            
            for i in range(ind,len(candidates)):
                if sum(path) > target:
                    return

                path.append(candidates[i])
                rec(path,i)
                path.pop()
        rec([],0)
        return res