# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # just do recursion and go till the end node and append
        # to the list finally check if the two list are same for the 
        # two graph

        temp2 = []  
        temp1 = []

        def rec1(root1):
            if root1 is None:
                return
            if not root1.left and not root1.right:
                temp1.append(root1.val)
            rec1(root1.left)
            rec1(root1.right)

        def rec2(root2):
            if root2 is None:
                return  
            if not root2.left and not root2.right:
                temp2.append(root2.val)
            rec2(root2.left)
            rec2(root2.right)

        rec1(root1)
        rec2(root2)
        

        return temp1 == temp2
        