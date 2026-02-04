class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        

        h = []
        sort_arr = []
        for i in range(len(profits)):
            sort_arr.append((capital[i], profits[i]))
        
        sort_arr.sort()
        h = []
        i = 0
        while k >0:
            while i <len(sort_arr) and sort_arr[i][0] <= w:
                heapq.heappush(h,-sort_arr[i][1])
                i = i+1
            if not h:
                break
            w = w + -heapq.heappop(h)
            k = k-1
        
        return w

