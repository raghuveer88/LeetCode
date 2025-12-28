class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # res = 0
        # i = 0
        # j = 0

        # while i < len(haystack):
            
        #     if haystack[i] == needle[j]:
                
        #         if j == len(needle)-1:
        #             return i-j
        #         j = j+1
        #     else:
        #         j = 0
        #     i = i+1        
        # return -1
        n = len(needle)
        i = 0

        
        while i <= len(haystack)-n:
            window = haystack[i:i+n]

            if window == needle:
                return i
            i = i+1
        
        return -1



            
