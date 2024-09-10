class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        self.edges = {(a, b) for a, b in connections}
        # Create an adjacency list
        self.neighbours = {city: [] for city in range(n)}
        self.visit = set()
        self.count = 0

        # Build the undirected graph (since it's undirected, add both ways)
        for a, b in connections:
            self.neighbours[a].append(b)
            self.neighbours[b].append(a)

        # DFS function
        def dfs(city):
            # Explore all the neighbours
            for neighbour in self.neighbours[city]:
                if neighbour in self.visit:
                    continue
                # Check if we need to reorder the edge
                if (neighbour, city) not in self.edges:
                    self.count += 1
                # Mark the neighbour as visited
                self.visit.add(neighbour)
                # Recursively call DFS
                dfs(neighbour)

        # Start DFS from city 0
        self.visit.add(0)
        dfs(0)
        return self.count
