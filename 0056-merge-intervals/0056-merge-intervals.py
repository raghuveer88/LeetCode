class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        if len(intervals) == 1:
            return intervals
        
        res = []
        
        j = 0
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end= intervals[i][1]
            while j+1< len(intervals) and intervals[j+1][0]  <= end:
                j = j+1
                end = max(end,intervals[j][1])

            res.append([start,end])
            i= j+1
            j= i

        return res
            

