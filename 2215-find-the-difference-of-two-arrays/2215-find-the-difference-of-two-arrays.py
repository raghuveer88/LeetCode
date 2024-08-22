class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Make sure to remove the duplicates and find the differences
    
        left = list(set(nums1) - set(nums2))
        right = list(set(nums2) - set(nums1))

        return [left,right]