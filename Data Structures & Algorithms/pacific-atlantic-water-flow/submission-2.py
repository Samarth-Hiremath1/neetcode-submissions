'''
bf:
    iterate through every element
    do dfs/bfs to figure out recursively if the path 
        connects to both oceans

optimal:
land -> ocean
ocean -> land

hashset for pac, atl

def dfs(r, c, seen, prevHeight):
    if (r,c) in seen, out of bounds, or too short:
        return
    
    add to seen
    do dfs on all 4 directions


for every elem top and bottom row:
    do dfs on top row --> add to pac
    do dfs on bottom row --> add to alt

for every elem top and bottom row:
    do dfs on top row --> add to pac
    do dfs on bottom row --> add to alt

res
for every elem in grid:
    if elem in both pac and alt:
        add to res

return res

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return 0
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        directions = [[1,0], [-1,0], [0, 1], [0,-1]]

        
        def dfs(r, c, seen, prevHeight):
            if((r, c) in seen or
               r < 0 or c < 0 or r == rows or c == cols or
               prevHeight > heights[r][c]):
               return
            seen.add((r, c))

            for dr, dc in directions:
                row, col = r+dr, c+dc
                dfs(row, col, seen, heights[r][c])


        
        for c in range(cols):
            # top row
            dfs(0, c, pac, heights[0][c])

            # bottom row
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            # left col
            dfs(r, 0, pac, heights[r][0])

            # right col
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res

        


