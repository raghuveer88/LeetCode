# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        #Just do recursion based on the direction is you are on left
        # then you only increment the length of you find a right
        # or you just keep the lenght 1
    
        def zigdsf(node, direction,length):
            if node is None:
                return 
            self.max_length = max(self.max_length,length)

            if direction == "left":
                zigdsf(node.left,"left",1)
                zigdsf(node.right,"right", length + 1)
            
            if direction == "right":
                zigdsf(node.right,"right",1)
                zigdsf(node.left,"left", length+1)

        

        self.max_length = 0
        zigdsf(root,"left",0)
        zigdsf(root,"right",0)
        return self.max_length

        