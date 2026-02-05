class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        res = 1

        for i in range(len(points)):
            p0 = points[i]
            count = defaultdict(int)

            for j in range(i+1,len(points)):
                p1 = points[j]

                if p1[0] == p0[0]:
                    slope = float(inf)
                    # count[float(inf)] += 1
                else:
                    slope = (p1[1]-p0[1])/(p1[0]-p0[0])
                count[slope] += 1
                res = max(res,count[slope]+1)
            
        return res
                    





        

