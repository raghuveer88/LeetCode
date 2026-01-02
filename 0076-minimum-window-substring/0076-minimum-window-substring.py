class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        have = Counter(t)
        seen = Counter()
        seen_count = 0
        have_count = len(have)
        j = 0
        res, reslen = (-1,-1), float("inf")


        for i in range(len(s)):
            seen[s[i]] += 1
                
            if s[i] in have and seen[s[i]] == have[s[i]]:
                seen_count +=1

            while seen_count == have_count:

                if (i-j+1) < reslen:
                    res = (j,i)
                    reslen = i-j+1
                seen[s[j]] -=1
                if s[j] in have and seen[s[j]] < have[s[j]]:
                    seen_count -= 1

                j += 1
        l,r = res
            
        return s[l:r+1] if reslen != float("inf") else ""
                