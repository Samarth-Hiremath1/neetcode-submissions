# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Optimal:
have 2 starting pointer:
    left at start - 1 (using dummy node before LL starts)
        (-1 because we want to be at n-1 node if we are removing nth node)
    right at n places a head of start

increment both by 1 until it reaches the end
remove nth node by making left's next to be left.next.next

return list

'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # initialize dummy + left + right 
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


