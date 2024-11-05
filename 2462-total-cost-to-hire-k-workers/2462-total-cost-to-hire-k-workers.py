class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        # for this poblem firstly take the first left elements and right elements of length candidates
        # put them in  a heap along with the cost,index and flag(which says it's left or right).
        # then take the min value in the heap and add it to total as you removed a element now 
        # (need to be done K times)you can add another element from costs array to the heap if the cost 
        # removed is in the min heap is left added then add the next left element if right 
        # then do it for right at the end return the total

        n = len(costs)
        h = []
        left = 0
        for i in range(candidates):
            heapq.heappush(h, (costs[left], left, 1))
            left = left + 1
        
        right = n-1
        for i in range(candidates):
            if right < left:
                break
            heapq.heappush(h, (costs[right], right, -1))
            right -= 1
        total = 0
        for i in range(k):
            c,index,flag = heapq.heappop(h)
            total = total + c

            if left<=right:
                if flag == 1:
                    heapq.heappush(h, (costs[left], left, 1))
                    left += 1
                elif flag == -1:
                    heapq.heappush(h,(costs[right],right,-1))
                    right -= 1
                
        return total

