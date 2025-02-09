# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0  # Start count from 0 to get the correct length
        
        # Count the total number of nodes
        while temp:
            temp = temp.next
            count += 1
        
        to_del = count - n  # Find the position from the start
        
        # If we need to remove the head node
        if to_del == 0:
            return head.next
        
        temp2 = head
        current = 0
        
        # Traverse to the node just before the one to delete
        while temp2 and current < to_del - 1:
            temp2 = temp2.next
            current += 1
        
        # Delete the target node
        if temp2 and temp2.next:
            temp2.next = temp2.next.next
        
        return head