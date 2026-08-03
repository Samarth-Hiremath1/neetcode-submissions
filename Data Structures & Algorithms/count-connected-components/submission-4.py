from collections import defaultdict
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()

        def bfs(node):
            q = deque()
            q.append(node)
            seen.add(node)

            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if nei not in seen:
                        q.append(nei)
                        seen.add(nei)
        
        res = 0
        for node in range(n):
            if node not in seen:
                bfs(node)
                res += 1
        return res