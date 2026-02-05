class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        total = digits[0]
        for i in range(1,len(digits)):
            total = total*10+digits[i]
        
        total += 1
        res = []
        while total>0:
            res.append(total%10)
            total = total//10
        
        res.reverse()

        return res


