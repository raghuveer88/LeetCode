# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        temp1 = dummy
        temp2 = dummy
        count = 1
        while count<=n:
            temp2 = temp2.next
            count = count+1
        
        while temp2.next:
            temp2 = temp2.next
            temp1 = temp1.next
        
        temp1.next = temp1.next.next

        return dummy.next

        
        


