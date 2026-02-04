class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = int(a,2)
        b = int(b,2)

        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a,b = without_carry, carry
        
        binary = ""
        if a == 0:
            return "0"
        else:
            while a > 0:
                binary = str(a%2) + binary
                a = a//2
            return binary


        
        