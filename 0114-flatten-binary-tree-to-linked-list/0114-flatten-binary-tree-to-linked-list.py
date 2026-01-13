# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        dummy = TreeNode(0)
        tail = dummy

        def rec(node):
            nonlocal tail
            if not node:
                return 
            
            tail.right = node
            tail = tail.right
            temp2 = tail.right
            temp = tail.left
            tail.left = None
            rec(temp)
            rec(temp2)

        rec(root)
        return dummy.right