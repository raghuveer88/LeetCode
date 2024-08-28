# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # so take three nodes pre, current and next then just assign
        # current.next to pre and update the current and next to the later
        # variables


        if not head or not head.next:
            return head
       
        pre = head
        current = head.next
        nex = current.next
        first = head

        while current and nex:
            
            current.next = pre

            pre = current
            current = nex  
            nex = current.next
        
        current.next = pre

        head = current
        first.next = None


        return head          
                
            
