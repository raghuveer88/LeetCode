class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # so here we can make the graph in such a way that a->b with a weight of 'x' and vice
        # versa with b->a as '1/x'. so lets take an example if the we have a->b as '2' then
        # b->c as '3' then a->c will be '2x3 =6' so this is how to find the values for queries
        # array. is you don't find a value which is not in equations then return -1 

        adj = collections.defaultdict(list)
        for i,eq in enumerate(equations):
            a,b = eq
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]])

        def bsf(src,target):
            if src not in adj or target not in adj:
                return -1
            q = deque()
            visit = set()
            q.append([src,1])
            visit.add(src)
            while q:
                n,w = q.popleft()
                if n == target:
                    return w
                for neighbour, weight in adj[n]:
                    if neighbour not in visit:
                        q.append([neighbour, w*weight])
                        visit.add(neighbour)
            return -1

        result = []
        for q in queries:
           result.append(bsf(q[0],q[1])) 
        
        return result