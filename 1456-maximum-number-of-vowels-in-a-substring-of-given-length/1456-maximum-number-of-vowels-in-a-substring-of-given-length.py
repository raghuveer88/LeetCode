class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = 'aeiouAEIOU'
        cur_vowel = s[:k]
        count = 0
        for char in cur_vowel:
            if char in vowels:
                count = count + 1
        result = count

        for i in range(1,len(s)-k+1):
            if s[i-1] in vowels:
                count = count -1
            if s[i+k-1] in vowels:
                count = count + 1
                result = max(result,count)
        return result