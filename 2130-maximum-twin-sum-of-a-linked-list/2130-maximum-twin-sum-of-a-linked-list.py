# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        # So the approach is to use a slow and fast pointer so make sure we go to
        # the middle with the slow pointer. basically if we move fast pointer twice 
        # and slow pointer once we will reach the middle point. Now try to reverse
        # the first half of array and add (temp will be the first element of the reversed)
        # return the max sum

        slow,fast = head,head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        res = 0
        while slow:
            res = max(res, prev.val+slow.val)
            slow = slow.next
            prev = prev.next
        
        return res

        

       






