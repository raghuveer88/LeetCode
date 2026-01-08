# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def rec(node,d):
            
            if not node:
                return d-1
            
            a = rec(node.left,d+1)
            b = rec(node.right,d+1)
            return max(a,b)  
            
        return rec(root,1)

            
        
