"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        

        oldtoNew = {}

        def rec(node):
            if not node:
                return None
            if node in oldtoNew:
                return oldtoNew[node]
            
            copy = Node(node.val)
            oldtoNew[node] = copy

            for n in node.neighbors:
                    copy.neighbors.append(rec(n))
            return copy
        return rec(node)


