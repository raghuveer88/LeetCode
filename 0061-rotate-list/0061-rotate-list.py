# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        steps = k%count
        if steps == 0:
            return head

        dummy = ListNode(0,head)
        temp1 = dummy
        temp2 = dummy

        while steps > 0:
            temp2 = temp2.next
            steps -= 1
        
        while temp2.next:
            temp2 = temp2.next
            temp1 = temp1.next
        
        
        first = temp1.next
        
        temp1.next = None
        temp2.next = head

        return first




