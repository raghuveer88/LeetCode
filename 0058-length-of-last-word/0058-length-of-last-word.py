class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()[-1]
        
        return len(a)