class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        visited = set()
        output = []

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            w = values[i]
            graph[a].append((b,w))
            graph[b].append((a,1/w))

        def rec(val1,val2,cost,visited):
            if val1 not in graph or val2 not in graph:
                return -1
            
            if val1 == val2:
                return cost
            visited.add(val1)
            for nei in graph[val1]:
                if nei[0] in visited:
                    continue
                res = rec(nei[0],val2,cost * nei[1],visited)
                if res != -1:
                    return res
            
            return -1
            
        for nei in queries:
            output.append(rec(nei[0],nei[1],1,set()))
                
        return output
            
