# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # if no root exists, return None
        if not root:
            return None
        
        # swap left and right nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursive call to the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root