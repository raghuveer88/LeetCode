"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        curr =head
        dummy = Node(0)
        tail = dummy
        addmap = {}
        while curr:
            tail.next = Node(curr.val)
            tail = tail.next
            addmap[curr] = tail
            curr = curr.next

        curr = head
        tail =  dummy
        while curr:
            tail = tail.next
            if curr.random == None:
                tail.random = None
            else:
                tail.random = addmap[curr.random]
            curr = curr.next
        
        return dummy.next
            
            
        
        