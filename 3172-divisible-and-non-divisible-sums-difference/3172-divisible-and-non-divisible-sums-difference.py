class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        start = 1
        num1 = 0
        num2 = 0
        while start <= n:
            if start % m == 0:
                num2 += start
            else:
                num1 += start
            start += 1

        return num1-num2