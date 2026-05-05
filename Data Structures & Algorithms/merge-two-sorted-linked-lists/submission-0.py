# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # adding dummy node to avoid edge case of having 
        # an empty LL
        dummy = ListNode()
        tail = dummy

        # while both LLs have content
        while l1 and l2:
            
            # check which list has a smaller value
            # if l1 smaller value, add l1's value and move it to the next position
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            # if l2 has the smaller value, add l2's value
            # and move it to the next position
            else:
                tail.next = l2
                l2 = l2.next
            
            # update tail pointer (why?)
            tail = tail.next

        # edge case where if one list is longer than the other
        # add the remaining values to the end of the list
        if l1:
            tail.next = l1

        elif l2:
            tail.next = l2

        return dummy.next