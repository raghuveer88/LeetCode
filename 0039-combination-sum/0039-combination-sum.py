class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []


        def rec(path,ind,rem):
            if rem == 0:
                res.append(path[:])
                return
            
            for i in range(ind,len(candidates)):
                if rem < 0:
                    return

                path.append(candidates[i])
                rec(path,i,rem-candidates[i])
                path.pop()
        rec([],0,target)
        return res