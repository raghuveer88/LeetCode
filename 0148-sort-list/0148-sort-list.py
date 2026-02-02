# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(l1,l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            tail.next = l1 if l1 else l2
            return dummy.next
        
        def sort(node):
            if not node or not node.next:
                return node
            
            fast=slow = node
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None

            left = sort(node)
            right = sort(slow)

            return merge(left,right)

        return sort(head)

            

            