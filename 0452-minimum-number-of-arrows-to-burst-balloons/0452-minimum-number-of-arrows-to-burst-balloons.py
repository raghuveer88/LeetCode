class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        count = 0
        i = 0
        j = 0
        while i<len(points):
            newInterval = points[i]
            while j+1 < len(points) and newInterval[1]>= points[j+1][0]:
                start = max(newInterval[0],points[j+1][0])
                end = min(newInterval[1],points[j+1][1])
                newInterval = [start,end]
                j = j+1
            
            count = count +1
            i = j+1
            j = i

        return count

# 1,6
# 2,8
# 7,12
# 10,16