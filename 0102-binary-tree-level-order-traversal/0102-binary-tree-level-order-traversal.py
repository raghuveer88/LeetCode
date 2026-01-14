# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        if not root:
            return []

        def rec(level):
            if not level:
                return

            next_level = []
            res = []
            for node in level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
                res.append(node.val)
            
            output.append(res)

            rec(next_level)
        
        rec([root])

        return output

