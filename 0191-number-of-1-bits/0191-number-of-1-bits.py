class Solution:
    def hammingWeight(self, n: int) -> int:
        
        def binary(n):
            if n == 0:
                return "0"
            count = 0
            while n >0:

                a = n%2
                if a == 1:
                    count += 1
                n = n//2
            return count
        

        return binary(n)