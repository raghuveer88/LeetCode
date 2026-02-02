# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return       

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

        def solve(lists):
            if not lists:
                return
            
            while len(lists)>1:
                merge_list = []
                for i in range(0,len(lists),2):
                    a = lists[i]
                    if i+1 < len(lists):
                        b = lists[i+1]
                    else:
                        b = None
                    merge_list.append(merge(a,b))
                lists = merge_list
            
            return lists[0]
        return solve(lists)
