# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # def printSubTree(node):
        #     if node is None:
        #         return 
        #     self.res.append(node.val)
        #     printSubTree(node.left)
        #     printSubTree(node.right)

        if root is None or root.val == val:
            return root
        
        # If the target value is less than the current node's value, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If the target value is greater than the current node's value, search in the right subtree
        return self.searchBST(root.right, val)