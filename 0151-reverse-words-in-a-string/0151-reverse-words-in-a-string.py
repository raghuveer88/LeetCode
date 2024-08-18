class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        senList = s.split()
        senList.reverse()
        return " ".join(senList)