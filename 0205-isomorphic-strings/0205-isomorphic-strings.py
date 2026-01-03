class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        
        for i in range(len(s)):
            if s[i] not in s_set:
                s_set[s[i]] = t[i]
            
            if t[i] not in t_set:
                t_set[t[i]] = s[i]
            
            if s[i] in s_set and t[i] != s_set[s[i]]:
                return False
            
            if t[i] in t_set and s[i] != t_set[t[i]]:
                return False

    #   b -> b
    #   a -> a
    #   d -> b
    #   c -> a

            
        
        return True




        
        