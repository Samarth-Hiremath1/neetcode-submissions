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

        islands = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()

            q.append((r,c))
            seen.add((r,c))

            while q:
                row, col = q.popleft()

                # check all adj. positions
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in seen):
                        q.append((r,c))
                        seen.add((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1

        return islands