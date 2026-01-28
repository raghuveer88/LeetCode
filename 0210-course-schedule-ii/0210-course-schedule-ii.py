class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = set()
        path = set()
        graph = defaultdict(list)
        output = []

        for i in range(len(prerequisites)):
            a = prerequisites[i][0]
            b = prerequisites[i][1]
            graph[b].append(a)

        def rec(node):
            visited.add(node)
            path.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    a = rec(nei)
                    output.append(nei)  
                    if not a:
                        return False
                elif nei in visited and nei in path:
                    return False
                 
            path.remove(node)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not rec(i):
                    return []
                output.append(i)
        
        output.reverse()
        return output