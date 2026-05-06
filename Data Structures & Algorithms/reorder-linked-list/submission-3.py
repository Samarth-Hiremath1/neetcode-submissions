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

        # seperate first and second halves
        second_half = slow.next
        slow.next = None
        
        # 4 -> 5 -> 6 -> None
        # reverse 2nd half:
        prev = None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            
            prev = second_half
            second_half = temp

        
        # merge 2 halfs
        first, second = head, prev
        while second:
            # save the next pointers b4 updating
            tmp1, tmp2 = first.next, second.next

            # update pointers
            first.next = second
            second.next = tmp1

            # move pointers forward
            first, second = tmp1, tmp2
