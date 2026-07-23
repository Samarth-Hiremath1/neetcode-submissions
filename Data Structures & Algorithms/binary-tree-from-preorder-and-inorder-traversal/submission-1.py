# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        given preorder + postorder
        use recursive dfs

        base case: empty, return None

        note: first element in preorder will be a root node
        thus, calculate middle point by finding it in the inorder list
            inorder.index[preorder[0]]
        
        everything to the left of mid = left subtree
        everything to the right of mid = right subtree

        return root
        '''

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

