class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        #just check the frequences of the letter and check if letters in word1
        # exists in word2 if they do then return True else return false
        
        res_dict = {}
        res2_dict = {}
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False

        for i in word1:
            if i in res_dict:
                res_dict[i] += 1
            else:
                res_dict[i] = 1

        for i in word2:
            if i in res2_dict:
                res2_dict[i] += 1
            else:
                res2_dict[i] = 1

        if sorted(res_dict.values()) == sorted(res2_dict.values()):
            return True
        else:
            return False

        