# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
       
        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        small_tail = small_dummy
        large_tail = large_dummy

        current = head
        while current:
            next_node = current.next
            current.next = None

            if current.val<x:
                small_tail.next = current
                small_tail = current
            else:
                large_tail.next = current
                large_tail = current
            
            current = next_node
        
        small_tail.next = large_dummy.next

        return small_dummy.next
        