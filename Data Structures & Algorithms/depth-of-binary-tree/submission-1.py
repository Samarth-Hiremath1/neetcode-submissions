# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Optimal solution: recursive DFS

at each node, add 1 (current node) + max(left subtree depth, right subtree depth)
recursive calls for each

'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        '''
        OPTIMAL SOLUTION
        # use recursive DFS
        
        # Base Case: if no node: return 0
        if not root:
            return 0

        # recurssive call
        # return 1 + max(dfs.left, dfs.right)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right ))

        '''


        '''
        iterative BFS

        travese level by level 
        count the # of levels we have

        return levels
        

        use queue

        add root node
        pop the node and replace it with its children
        +1 to the level number if it has children

        keep repeating until all nodes get popped
        return the level number

        ---

        # base case
        if not root:
            return 0
        
        # initialize level + deque (deque bc we want flexibility with order)
        level = 0
        q = deque([root])

        while q:
            # remove every element in the que + add children (travese level + add next level)
            for i in range(len(q)):
                # add node's children if they aren't Null
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level += 1
        return level
        
        '''
        


        '''
        iterative dfs
        visit every single node via stack (collect node + depth)
        find the node with greatest depth and return that

        add root node to stack
        pop it and add its children
        pop
        '''
        if not root:
            return 0

        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return res