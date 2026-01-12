"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        # ans = Node(root.val)

        def rec(level):
            if not level:
                return 
            
            for i in range(len(level)):
                if i+1 < len(level):
                    level[i].next = level[i+1]
                else:
                    level[i].next = None 

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            rec(next_level)

        rec([root])
        return root