class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        left = bin(left)[2:].zfill(32)
        right = bin(right)[2:].zfill(32)

        i = 0
        res = 0
        while i < 32:
            if left[i] == right[i]:
                res += int(left[i]) * 2**(31-i)
                i = i+1
                
            else:
                break
        
        return res

