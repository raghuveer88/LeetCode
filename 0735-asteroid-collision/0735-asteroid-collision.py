class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        #First take an empty stack thenthe collision happens only if 
        # There is a positive and negative. In other cases it woon't happen
        # So just add eacch element in to the stack and verify the case

        stack = []

        for i in asteroids:
            # if not stack:
            #     stack.append(i)
            while stack and stack[-1] > 0 and i < 0:
                if abs(i) > abs(stack[-1]):
                    stack.pop()
                elif abs(i) < abs(stack[-1]):
                    i = 0
                else:
                    stack.pop()
                    i = 0
            if i != 0:
                 stack.append(i)

        return stack



       