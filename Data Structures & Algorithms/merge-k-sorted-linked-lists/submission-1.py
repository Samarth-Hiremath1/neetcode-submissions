# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
BF:
Manually go through each list one by one and merge everything
T: O(n*k)
S: O(?)
'''

'''
optimal: merge sort

1. check edge cases (empty list or len 0 list)
2. while len(lists) is atleast 1
    a. initialize mergedList = []
    b. for every 2 lists (0, len(lists), 2):
            merge 2 lists


T: O(n log k)
S: O(?)


'''

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]

                # ensuring l2 isn't past the end of the list
                if(i+1 < len(lists)): 
                    l2 = lists[i+1]
                else: 
                    l2 = None

                # merge and append
                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):

        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if(l1.val < l2.val):
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2

        return dummy.next



