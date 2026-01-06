# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        curr = head
        beforeLeft = dummy

        n = 1
        while n < left:
            beforeLeft = curr
            curr = curr.next
            n += 1

        leftNode = curr
        prev = None
        while n <= right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            n += 1

        beforeLeft.next = prev     
        leftNode.next = curr      

        return dummy.next


        


            
        