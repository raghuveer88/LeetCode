class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        select = defaultdict(set)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    select['row'].add(i)
                    select['col'].add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in select['col']:
                    matrix[i][j] = 0
                if i in select['row']:
                    matrix[i][j] = 0
        
        return matrix