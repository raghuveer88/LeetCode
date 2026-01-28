class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        path = set()

        graph = defaultdict(list)
        
        for i in range(len(prerequisites)):
            a = prerequisites[i][0]
            b = prerequisites[i][1]
            graph[b].append(a)

        def rec(node):
            visited.add(node)
            path.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if not rec(nei):
                        return False
                elif nei in visited and nei in path:
                    return False
            path.remove(node)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not rec(i):
                    return False
        return True
                    
