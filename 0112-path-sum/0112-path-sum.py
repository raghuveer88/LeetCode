# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False
        
        def rec(node,curr_sum):
            if node:
                curr_sum = curr_sum + node.val
                if not node.left and not node.right and curr_sum == targetSum:
                    return True
            
            if not node:
                return False
            
            
            a = rec(node.left, curr_sum)
            b = rec(node.right,curr_sum)

            return a or b

        return rec(root, 0)

