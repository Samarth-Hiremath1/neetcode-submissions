# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        toirtise and hare method
        fast and slow pointers. if cycle exists, 
        fast pointer will loop and catch back up to slow pointer
        
        T: O(n)
        S: O(1)

        '''

        # both pointers start at the same position
        slow, fast = head, head

        
        # move slow by 1 place
        # move fast by 2 places
        # while fast and the next pointer still exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        # no cycle
        return False