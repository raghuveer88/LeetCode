class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def fact(n):
            if n == 0 or n ==1:
                return 1
            return n*fact(n-1)
        

        res = fact(n)
        # print(res)
        count = 0
        while res%10 == 0 and res != 0:
            count = count+1
            res = res//10
        
        return count
