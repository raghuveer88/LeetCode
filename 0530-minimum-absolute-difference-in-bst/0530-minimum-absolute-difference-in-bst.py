# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float("inf")
        prev = None
        def rec(node):
            nonlocal ans,prev
            if not node:
                return 
            
            rec(node.left)
            if prev is not None:
                ans = min(ans, node.val-prev)
            prev = node.val
            rec(node.right)

           
        rec(root)
        return ans



            

        rec(root)
        return res