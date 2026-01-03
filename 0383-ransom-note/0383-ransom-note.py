class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rans = Counter(ransomNote)
        mags = Counter(magazine)

        for k,v in rans.items():
            if k not in mags or mags[k] < rans[k]:
                return False

        
        return True
