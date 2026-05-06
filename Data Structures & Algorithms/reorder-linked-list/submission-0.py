# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
BF: 
convert LL to an array
2 pointers (start, end)
    iterate and reconstruct new LL
'''

'''
Optimal:
2 phases:
    1. reverse the second half
        a. identify second half via slow & fast pointers
        b. 

    2. merge 2 lists
        a. 2 pointers at start and end
        b. 
'''


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # identify first and second half of the LL
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        
        # seperate first and second halves
        slow.next = None

        prev = None

        # reverse 2nd half of list
        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp
        
        # merge 2 halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2





