# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # iterative approach --> 2 pointers
        T: O(n)
        S: O(1)
        prev, curr = None, head

        while curr:
            # temp variable storing the 3rd positions location
            # ex: [prev, curr, temp_next]
            temp_next = curr.next
            
            # change pointer direction
            curr.next = prev
            
            # move pointers
            prev = curr
            curr = temp_next
        return prev
        '''

        # recurrsive approach
        # T: O(n)
        # S: O(n)

        # if head is null
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead

