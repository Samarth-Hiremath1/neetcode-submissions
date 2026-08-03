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
            return None

        rows, cols = len(heights), len(heights[0])
        
        pac = set()
        atl = set()

        directions = [[1,0],[-1,0], [0,1], [0,-1]]

        def dfs(r, c, seen, prevHeight):
            if(r not in range(rows) or
               c not in range(cols) or
               (r, c) in seen or
               heights[r][c] < prevHeight):
               return
            seen.add((r, c))

            for dr, dc in directions:
                row, col = r+dr, c+dc
                dfs(row, col, seen, heights[r][c])


        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

