class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)-1
        if size <=0:
            return 0

        queue = deque()
        queue.append(0)
        jump = 0
        visited = [False]*len(nums)
        visited[0] = True

        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                reach = i+nums[i]
                

                if reach >= size:
                    return jump+1
                
                for j in range(i+1,reach+1):
                    if j<=size and not visited[j]:
                        queue.append(j)
                        visited[j] = True
            jump = jump + 1
        



        



