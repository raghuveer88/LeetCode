class Solution:
    def romanToInt(self, s: str) -> int:
        # This code is self explanatory just go throught the code it has got if statements
        # which handles the logic.
        res = 0
        mydict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        i = 0
        while i < len(s):
            if i + 1 < len(s) and (
                (s[i] == "I" and s[i+1] in {"V", "X"}) or 
                (s[i] == "X" and s[i+1] in {"L", "C"}) or 
                (s[i] == "C" and s[i+1] in {"D", "M"})
            ):
                    res = res + mydict[s[i+1]] - mydict[s[i]]
                    i = i + 2
                    continue
            else:
                res = res + mydict[s[i]]
            i = i + 1
            
        return res
