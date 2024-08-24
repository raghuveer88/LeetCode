class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # JUST ADD THE ELEMENTS TO STACK IF IT'S NOT *
        # AND IF IT'S * THEN POP THE ELEMENT 

        s_list = list(s)
        stack = []

        for i in s_list:
            if i == "*" and stack:
                stack.pop()
            elif i != "*":
                stack.append(i)

        return "".join(stack)

        
        