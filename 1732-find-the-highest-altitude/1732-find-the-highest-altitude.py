class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # just add the result[i] and gain[i] get the max altitude

        result = [0]

        for i in range(len(gain)):
            result.append(result[i] + gain[i])

        print(result)

        return max(result)