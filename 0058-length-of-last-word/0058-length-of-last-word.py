class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(" ")
        res = 0
        for i in a:
            if i != "":
                res = len(i)
        return res