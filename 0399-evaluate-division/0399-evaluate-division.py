class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a,b), val in zip(equations,values):
            graph[a].append((b,val))
            graph[b].append((a,1/val))

        def dsf(curr, target, visited):
            if curr == target:
                return 1

            visited.add(curr)
            for nei,w in graph[curr]:
                if nei in visited:
                    continue
                res = dsf(nei,target,visited)
                if res != -1:
                    return w*res
                
            return -1

        ans = []
        for src, target in queries:
            if src not in graph or target not in graph:
                ans.append(-1)
            elif src == target:
                ans.append(1)
            else:
                ans.append(dsf(src,target,set()))
    
        return ans
