class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        i = len(digits)-1
        if digits[i] != 9:
            digits[i] = digits[i]+1
            return digits
        
        else:
            while i>=0 and digits[i] == 9:
                carry = 1
                digits[i] = 0
                i = i-1
            if i >=0 and carry:
                digits[i] += carry
                res = digits
            else:
                res.append(carry)
                res.extend(digits)
        return res

                


