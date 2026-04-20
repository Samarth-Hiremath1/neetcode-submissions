# BF
'''
1. check all rows
    a. for each index row from 0-8
    for each column index i from 0-8
        skip if cell is "."
        if the value is already in seen, return false
        else, add to hashmap

2. check all columns:
    ...

3. check all 3x3 boxes
    a. number all boxes from 0-8
    b. for each square:
        create an empty set seen
        for i in 0..2, and j in 0..2
            computer
                row = (square // 3) * 3 + i
                col = (square % 3) * 3 + j
            skip cell if empty
            if the value is already in seen, return false
            else add to seen

'''


# Hashmap
'''
check everything in one pass
1. create 3 hashmaps:
    rows[r]
    cols[c]
    squares[(r // 3, c // 3)]

2. loop through every cell in the board
    a. skip empty
    b. let val = digit in cell
    c. if val is already in any of the hashmaps, return false
    d. else add digit to all 3 sets

3. return true

'''



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if (board[r][c] == "."):
                    continue
                if(board[r][c] in rows[r] or 
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r//3, c//3)]):
                   return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True



