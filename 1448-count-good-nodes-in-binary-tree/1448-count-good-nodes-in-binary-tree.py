# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # when your visiting each node check if the current node is greater 
        # Than the existing max value in the path only then increase the count
        # or else don't. Since we need to Check each path we need to do DFS approach

        def dsf(node, maxValue):
            if node is None:
                return 0
            
            if node.val >= maxValue:
                count = 1
            else:
                count = 0
            maxValue = max(node.val,maxValue)
            count = count + dsf(node.left,maxValue)
            count = count + dsf(node.right,maxValue)

            return count

        return dsf(root,root.val)
                

