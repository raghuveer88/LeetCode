# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        list1 = ListNode()
        list2 = ListNode()
        temp = list2
        dummy = list1

        curr = head
        while curr:
            if curr.val < x:
                list1.next = curr
                list1 = list1.next
            elif curr.val >= x:
                list2.next = curr
                list2 = list2.next
            curr = curr.next
        # list1.next = None
        list2.next = None

        
        list1.next = temp.next

        return dummy.next