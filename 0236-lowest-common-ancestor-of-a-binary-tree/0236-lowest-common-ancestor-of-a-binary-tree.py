# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def rec(node):
            if not node:
                return 
            
            if node == p or node == q:
                return node
            
            a = rec(node.left)
            b = rec(node.right)

            if not a and b:
                return b
            if not b and a:
                return a
            if a and b:
                return node
        
        return rec(root)


            