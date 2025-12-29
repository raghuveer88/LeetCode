class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0 
        i = 0
        check = set()

        for j in range(len(s)):
            if s[j] not in check:
                res = max(res,j-i+1)
                check.add(s[j])
            
            else:
                while s[i] != s[j]:
                    check.remove(s[i])
                    i=i+1
                i = i+1
                res = max(res,j-i+1)
        
        return res
                    
