class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # First do the heap sort (max heap sort). which means the root should be larger than the
        # child nodes. Once sorted pop the kth element to the kth largest element
        
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        # print(max_heap)
        result = 0
        for i in range(k):
            result = -heapq.heappop(max_heap)
        
        return result