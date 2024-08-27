# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # pretty simple you just need to alternatively maintain two odd and 
        # even pointers and keep attaching them alternatively

        if not head:
            return head
       
        odd = head
        even = head.next
        first_even = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = first_even

        return head
        
       


        
        # odd.next = first_even
        # head = odd

        print(odd)
        print(even)

        return head