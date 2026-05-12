# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # T: O(p + q)

        '''
        Solution:
        go through all different edge cases node by node for each tree
        '''
        # if both trees are empty
        if not p and not q:
            return True
        
        # if only 1 is null
        if not p or not q:
            return False

        # if values aren't the same
        if p.val != q.val:
            return False

        # recursive step
        # check the same edge cases for both subtrees
        return (self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right))