'''
iterate through the adj. matrix

if island and not prev. visited:
    bfs
    islands += 1

return islands
'''

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        seen = set()
        islands = 0

        directions = [[1,0], [-1,0], [0, -1], [0,1]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            seen.add((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if(r in range(rows) and
                       c in range(cols) and
                       grid[r][c] == "1" and
                       (r,c) not in seen):
                        seen.add((r,c))
                        q.append((r, c))


        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands



