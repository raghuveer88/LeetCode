class Solution(object):
    
    def reverseVowels(self,s):
        """
        :type s: str
        :rtype: str
        """
        stringVowels = []
        revVowel = []
        index = []
        for i in range(len(s)):
            if s[i] in ('a','e','i','o','u','A','E','I','O','U'):
                stringVowels.append(s[i])
                index.append(i)
        
        # stringVowels.reverse()
        for i in range(len(stringVowels),0,-1):
            revVowel.append(stringVowels[i-1])
            
        for i in range(len(revVowel)):
            s = list(s)
            s[index[i]] = revVowel[i]
        s = ''.join(s)
        
        return  s
