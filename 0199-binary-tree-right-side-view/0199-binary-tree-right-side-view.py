# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # it is bsf use the queue to solve the problem
        # go level by level and append the last node to the result
        
        res = []

        q = deque()
        q.append(root)
        
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    temp.append(node.val)
            if temp:
                res.append(temp[-1])
        return res
            