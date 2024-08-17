class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(i):
            b = i
            a = max(len1,len2)
            while b:
                a,b = b, a%b
                gcd = a
            return a
        
        
        base = gcd(min(len1,len2))
        output = str1[:base]
        return output

