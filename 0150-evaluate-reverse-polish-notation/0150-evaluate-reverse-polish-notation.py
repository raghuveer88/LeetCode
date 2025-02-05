class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token in {"+", "-", "*", "/"}: 
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b)) 
            else:
                stack.append(int(token))  
        
        return stack.pop()