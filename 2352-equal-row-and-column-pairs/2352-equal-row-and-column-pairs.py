class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # This is my approach you can do it more simplerly by
        # making the row as key and the no:of times the row repeted 
        # as value then you can transpose the matrix 
        # and search of the column in as key in row key
        # and if it exist just add the counts
        
        col_dict = {}
        row_dict = {}
        count = 0

        for i in range(len(grid)):
            row_dict[i] = grid[i]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i not in col_dict:
                    col_dict[i] = [grid[j][i]] 
                else:
                    col_dict[i].append(grid[j][i])
        
        for i in range(len(row_dict)):
            for j in range(len(col_dict)):
                if col_dict[i] == row_dict[j]:
                    count += 1
        

        return count
            