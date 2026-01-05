class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for c in tokens:
            if c in {"+","-","*","/"}:
                b = int(stack.pop())
                a = int(stack.pop())
                if c == "+":
                    res = a+b
                elif c == "-":
                    res = a-b
                elif c == "*":
                    res = a*b
                elif c == "/":
                    res = a/b
                stack.append(res)
            else:
                stack.append(c)
            
        ans = stack.pop()

        return int(ans)