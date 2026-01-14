# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []

        def rec(level):
            if not level:
                return 
            
            next_level = []
            avg = 0
            count = 0
            for node in level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
                avg += node.val
                count += 1
            output.append(avg/count)

            rec(next_level)
        
        rec([root])

        return output
            