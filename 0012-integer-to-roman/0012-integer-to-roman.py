class Solution:
    def intToRoman(self, num: int) -> str:
        # First for sums like this create a map then using the map just try to solve it 
        map = {
            1000: 'M',
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        res = ""
        for k,v in map.items():
            while num >= k:
                res += v
                num -= k

        return res