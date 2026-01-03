class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()

        p_set = {}
        s_set = {}

        if len(pattern) != len(s_list):
            return False


        for i in range(len(pattern)):

            if pattern[i] in p_set and p_set[pattern[i]] != s_list[i]:
                return False
            if s_list[i] in s_set and s_set[s_list[i]] != pattern[i]:
                return False

            p_set[pattern[i]] = s_list[i]
            s_set[s_list[i]] = pattern[i]

        return True

        