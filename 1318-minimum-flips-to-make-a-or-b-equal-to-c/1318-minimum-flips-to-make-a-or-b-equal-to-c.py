class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flip = 0

        while a>0 or b>0 or c>0:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            if cbit == 1:
                if(abit | bbit != 1):
                    flip += 1
            else:
                if abit != 0:
                    flip +=1
                if bbit != 0:
                    flip += 1

            a = a>>1
            b = b>>1
            c = c>>1
        return flip


        # 1000
        # 0011

        # 0101