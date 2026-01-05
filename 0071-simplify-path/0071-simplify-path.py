class Solution:
    def simplifyPath(self, path: str) -> str:
        input = path.split('/')
        stack = []
        for c in input:
            if c == "" or c == ".":
                continue
            if c == "..":
                if stack:
                    stack.pop()
                    continue
                else:
                    continue
            else:
                stack.append(str(c))
    
        return "/"+"/".join(stack)

        