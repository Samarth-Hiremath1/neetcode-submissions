# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            # split or 
            # p/q is curr
            else:
                return curr

        
        
        
        
        
        
        
        
        
        
        
        '''
        curr = root

        while curr:
            # if both nodes are greater than current root node, 
            # both lie in the right side
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            # if both nodes are less than current root node,
            # both nodes lie on left side
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            # else if either p or q == current OR there is a split,
            # you are already at the ancestor
            else:
                return curr
        '''