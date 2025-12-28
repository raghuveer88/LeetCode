class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        a = "".join(ch.lower() for ch in s if ch.isalnum())

        # print(a)

        l = 0
        r = len(a)-1

        while l<r:
            if a[l] != a[r]:
                return False
            else:
                l = l+1
                r = r-1
        
        return True