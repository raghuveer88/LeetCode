# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # there are three cases since it is a binary tree
        # first if the key is last node then check right or left is empty
        # if left them assign the parent to right and vice-versa
        # if the key has both left and right child then go the right child lowest
        # node and replace the key with that node and delete the node original place
        def delNode(node,key):
            if node is None:
                return node
            if key < node.val:
                node.left = delNode(node.left,key)
            elif key > node.val:
                node.right = delNode(node.right,key)
            else:
                if node.right is None:
                    return node.left
                if node.left is None:
                    return node.right
                node.val = minValue(node.right)
                node.right = delNode(node.right,node.val)

            return node
        


        def minValue(node):
            minVal = node.val
            while node is not None:
                minVal = node.val
                node = node.left
            return minVal 
        
        return delNode(root,key)