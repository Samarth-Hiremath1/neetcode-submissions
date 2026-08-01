"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''

if not Node:
    return none

create hashmap: old -> newCopy

def dfs(node):
    if node in hashmap:
        return prev.copied.newNode

    new = Node(node.val)
    update hashmap
    for nNode in node.neighbors:
        new.neighbhors(dfs(nNode))
    return new

return dfs(node)

'''


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            new = Node(node.val)
            oldToNew[node] = new        
            for nNode in node.neighbors:
                new.neighbors.append(dfs(nNode))
            
            return new
        
        return dfs(node)




