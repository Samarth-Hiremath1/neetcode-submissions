"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''

hashmap: oldToNew

dfs:
    if node exists in oldToNew
        return oldToNew[node]
    
    # copy value
    new = Node(node.val)

    # copy neighbors
    for neiNodes in node.neighbors:
        new.neighbors.append(dfs(neiNodes))
    
    return new

dfs(node)

'''


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            # copy the value
            new = Node(node.val)
            oldToNew[node] = new

            # copy the neighbors
            for nei in node.neighbors:
                new.neighbors.append(dfs(nei))
            
            return new
        
        return dfs(node)

        
        
        