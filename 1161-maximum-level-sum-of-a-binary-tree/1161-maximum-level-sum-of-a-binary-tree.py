# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # so just go to each level in the BSF using a queue then
        # just add all the sum and check if it the greatest 
        # if yes just track the level number
        res_lev = 0
        q = deque()
        q.append(root)
        level = 0
        current_sum = float('-inf')
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            level += 1
            if temp and sum(temp) > current_sum:
                current_sum = sum(temp)
                res_level = level
            
        return res_level
        

        