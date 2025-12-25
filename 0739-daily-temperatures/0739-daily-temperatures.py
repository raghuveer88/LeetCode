class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        m = len(temperatures)
        ans = [0]*m
        stack = []

        for i,j in enumerate(temperatures):
            while stack and stack[-1][1] < temperatures[i]:
                a,b = stack.pop()
                ans[a] = i-a
            stack.append((i,temperatures[i]))

        return ans



# ans = [1,1,4 ,2 ,1 , 1, ]