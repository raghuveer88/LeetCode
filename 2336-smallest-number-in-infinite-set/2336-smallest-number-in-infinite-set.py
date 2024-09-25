class SmallestInfiniteSet(object):

# as the range is till 1000 create an array with 1-1000 values and each time
# popsmallest is called pop the number if addback is called check if the num
# is already there in the heap if not add it.

    def __init__(self):
        self.nums = [i for i in range(1,1001)]
        self.set_nums = set(self.nums)
        heapq.heapify(self.nums)

    def popSmallest(self):
        """
        :rtype: int
        """
        poped =  heapq.heappop(self.nums)
        self.set_nums.remove(poped)
        return poped

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.set_nums:
            heapq.heappush(self.nums,num)
            self.set_nums.add(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)