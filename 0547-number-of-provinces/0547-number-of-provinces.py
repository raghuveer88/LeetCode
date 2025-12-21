class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        total_nodes = len(isConnected)
        visited = [False]*total_nodes

        def dsf(city):
            visited[city] = True
            for j in range(total_nodes):
                if not visited[j] and isConnected[city][j] == 1:
                    dsf(j)
        
        provinces = 0
        for i in range(total_nodes):
            if not visited[i]:
                provinces += 1
                dsf(i)
        return provinces
