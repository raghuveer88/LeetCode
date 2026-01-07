# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        map = Counter()
        temp = head
        while temp:
            map[temp.val] = map[temp.val]+1
            temp = temp.next
        
        dummy = ListNode(0)
        temp = dummy
        temp2 = head
        while temp2:
            if map[temp2.val] < 2:
                temp.next = temp2
                temp = temp.next
                
            temp2 = temp2.next
        temp.next = None
        
        return dummy.next
        