# to solve this problem first we need to pair num1 and num2 and 
# sort the array of nums2 along with the num1
# now you know the smallest value in num2 will be the kth element only
# we just need to alter the nums1 sum. check the code you'll understand

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pairs = sorted(pairs,key = lambda p:p[1], reverse = True)

        minHeap = []
        n1sum = 0
        res = 0

        for n1,n2 in pairs:
            n1sum += n1
            heapq.heappush(minHeap,n1)

            if len(minHeap) >k:
                n1pop = heapq.heappop(minHeap)
                n1sum -= n1pop

            if len(minHeap) == k:
                res = max(res, n1sum * n2)

        return res


