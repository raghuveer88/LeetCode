# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # ✅ Handle edge case where there's 0 or 1 node
            return head

        temp = head.next  # ✅ Move temp assignment inside the valid condition
        res = head

        while temp and head:
            head.val, temp.val = temp.val, head.val  # ✅ Swap values
            if not temp.next or not head.next.next:  # ✅ Prevent accessing None
                break
            head = head.next.next
            temp = temp.next.next

        return res