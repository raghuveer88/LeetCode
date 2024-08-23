class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # just put the values in a dictionary(hashmap) then check the frequence

        frequence = {}

        for i in arr:
            if i in frequence:
                frequence[i] += 1
            else:
                frequence[i] = 1

        if len(frequence.values()) != len(set(frequence.values())):
            return False
        else:
            return True
        