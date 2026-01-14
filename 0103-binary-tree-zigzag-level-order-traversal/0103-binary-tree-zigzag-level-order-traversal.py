# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root:
            return []

        def rec(level,count):
            if not level:
                return

            next_level = []
            res = []
            
            for i in range(len(level)):
                if level[i].left: next_level.append(level[i].left)
                if level[i].right: next_level.append(level[i].right)
            if count%2 == 0:
                for node in reversed(level):
                    res.append(node.val)
            else:
                for node in level:
                    res.append(node.val)
            output.append(res)

            rec(next_level,count+1)
        
        rec([root],1)
        return output
