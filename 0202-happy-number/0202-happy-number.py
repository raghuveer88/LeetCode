class Solution:
    def isHappy(self, n: int) -> bool:
        hash = set()
        count = 0
        while count !=1:
            while n > 0:
                temp = n%10
                count =  count + temp**2
                n = n//10
            if count == 1:
                return True
            elif count in hash:
                return False
            else:
                hash.add(count)
            n = count
            count = 0           