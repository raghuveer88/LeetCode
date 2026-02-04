class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []        

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.left,-num)

        
        if not self.right or -self.left[0] > self.right[0]:
            a = -heapq.heappop(self.left)
            heapq.heappush(self.right,a)
        
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                a = -heapq.heappop(self.left)
                heapq.heappush(self.right,a) 
            else:
                a = heapq.heappop(self.right)
                heapq.heappush(self.left,-a) 



        

    def findMedian(self) -> float:
        # print(self.left,self.right)
        if len(self.left)> len(self.right):
            return -self.left[0]
        elif len(self.left)< len(self.right):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()