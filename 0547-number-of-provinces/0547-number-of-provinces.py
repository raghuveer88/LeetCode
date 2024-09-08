class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # You maintain a visited set in which you add all the visited nodes
        # first go through the first node and find all the attachments or paths to it
        # if a path exist to another node now go to that node add it to vistited set 
        # and try to find all the paths to it.
        # if a new node is there which is not visited then you need to increase the 
        # provinces

        def dfs(start):
            visited.add(start)
            for neighbor in range(len(isConnected)):
                if isConnected[start][neighbor] and neighbor not in visited:
                    dfs(neighbor)
        
        visited = set()
        provinces = 0
        for start in range(len(isConnected)):
            if start not in visited:
                provinces += 1
                dfs(start)

        return provinces
            