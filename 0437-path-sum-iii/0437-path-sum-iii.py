# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # It is a double Deepth first search. You go to every node and start calculating
        # the sum of all the paths till the end from that node (top to bottom)
        # if any path sum matches the target sum then increase the count

        def dfs(node,current_sum):
            if node is None:
                return
            current_sum += node.val
            if current_sum == targetSum:
                self.count += 1
            dfs(node.left,current_sum)
            dfs(node.right,current_sum)


        def ddfs(node):
            if node is None:
                return 
            dfs(node,0)
            ddfs(node.left)
            ddfs(node.right)
        self.count = 0
        ddfs(root)
        return self.count



        