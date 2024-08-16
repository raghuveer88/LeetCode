class Solution(object):

    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1Len = len(word1)
        word2Len = len(word2)
        i = 0
        j = 0
        result = ""
        while i<word1Len or j<word2Len :
            if i < word1Len:
                result = result + word1[i]
                i += 1
            if j < word2Len:
                result = result + word2[j]
                j = j+1
        return result

        