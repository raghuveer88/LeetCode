# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #This question is also pretty straight forward you just need travers the linked
        # list then put it in the array then reverse it then add it then put the 
        # new summend value in an array and reverse it and make it to a linked list
        l1_arr = []
        temp = l1
        while temp:  # Fixed: Include last node
            l1_arr.append(temp.val)
            temp = temp.next
        
        l2_arr = []
        temp2 = l2
        while temp2:  # Fixed: Include last node
            l2_arr.append(temp2.val)
            temp2 = temp2.next

        # Reverse and convert to integers
        l1_arr.reverse()
        l2_arr.reverse()

        l1_int = int("".join(map(str, l1_arr)))  # Fixed: Removed redundant list comprehension
        l2_int = int("".join(map(str, l2_arr)))

        res = l1_int + l2_int
        res = [int(digit) for digit in str(res)]
        res.reverse()

        # Create new linked list
        head = ListNode(res[0])  # Fixed: Removed `l3.head`
        temp3 = head
        for i in res[1:]:
            temp3.next = ListNode(i)
            temp3 = temp3.next
        
        return head 