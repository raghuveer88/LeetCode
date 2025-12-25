class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1],x[0]))

        start = points[0][0]
        prev_end = points[0][1]
        count = 1
        for i in range(1,len(points)):
            if prev_end < points[i][0]:
                count += 1
                start = points[i][0]
                prev_end = points[i][1]

        return count

