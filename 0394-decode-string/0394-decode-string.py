class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # So the steps would be add all the elements to the stack until you find
        # ] if you find it just get the substring and number before the substring
        # then multiply the substring and append it to the stack
        

        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                sub_string = ""
                while stack[-1] != '[':
                    sub_string = stack.pop() + sub_string
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*sub_string)
        
        return "".join(stack)


