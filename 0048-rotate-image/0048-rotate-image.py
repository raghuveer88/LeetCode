import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = [[] for _ in range(len(matrix[0]))]

        for i in range(len(matrix)-1,-1,-1):
            for ele in range(len(matrix[i])):
                # print(res[ele])
                res[ele].append(matrix[i][ele])
        matrix[:] = res
        return matrix

        

        