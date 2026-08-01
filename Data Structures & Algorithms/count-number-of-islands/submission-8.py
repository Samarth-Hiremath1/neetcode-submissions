'''
iterate through each island

bfs to add all islands parts to seen

recursive on all [r][c] combos

'''
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        seen = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    if((r+dr) in range(rows) and
                       (c+dc) in range(cols) and 
                       (r+dr, c+dc) not in seen and
                       (grid[r+dr][c+dc] == "1")):
                       q.append((r+dr, c+dc))
                       seen.add((r+dr, c+dc))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    bfs(row, col)
                    islands += 1

        return islands

        

