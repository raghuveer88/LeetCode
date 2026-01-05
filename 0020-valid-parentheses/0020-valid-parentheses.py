class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for b in s:
            
            if stack and b == ")":
                temp= stack.pop()
                if temp != "(":
                    return False
            elif stack and b == "}":
                if stack.pop() != "{":
                    return False
            elif stack and b == "]":
                if stack.pop() != "[":
                    return False
            else:
                stack.append(b)
            
        # print(len(stack))
        if stack:
            return False
        else:
            return True
