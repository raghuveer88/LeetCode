class Solution:
    def reverseBits(self, n: int) -> int:
        
        def binary(n):
            if n == 0:
                return '0'
            binary = ""
            while n > 0:
                binary = str(n%2) + binary
                n = n//2
            return binary
        

        input = binary(n)
        a = len(input)
        while a < 32:
            input = "0"+ input
            a = a+1
        input = input[::-1]
        return int(input,2)
