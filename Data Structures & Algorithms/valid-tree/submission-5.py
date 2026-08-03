'''
edge case: empty n --> return True

create adj. list

iterate through each one exactly once, while tracking seen setlist

def dfs(node, prev):
    if node in seen: --> loop
        return False
    
    add node to seen
    dfs on all neighbors
    for neighborNode of node:
        if neighborNode == node:
            continue
        if dfs(neighborNode, node) == False:
            return False
    
    return true

if dfs(0,-1) and n==len(seen):
    return True
else:
    return False


'''


'''
adj. list

seen = set()

def dfs(node, prev):
    if node in seen:
        return False
    seen.add(node)
    add all neighbors via dfs

if dfs(node, prev) and len(seen)==n:
    return true

'''

'''
if not n: return True
adj. list

seen = set()

def dfs(node, prev):
    if in seen return False
    add to seen
    for nei:
        if nei = prev:
            continue
        dfs(nei, node)

return dfs(0,-1) and n == len(seen)
'''

from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not edges:
            return True

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        seen = set()

        def dfs(node, prev):
            if node in seen:
                return False
            
            seen.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if nei in seen:
                    return False
                dfs(nei, node)
            return True

        return dfs(0,-1) and n == len(seen)
