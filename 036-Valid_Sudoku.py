'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
    
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board_transpose = [list(x) for x in zip(*board)]
        board_transpose = [[0]*9 for _ in range(9)]
        for row in range(9):
            for col in range(9):
                board_transpose[col][row] = board[row][col]
        
        for row in range(9):
            valid_row = self.validate_row(board[row])
            if not valid_row:
                return False
            valid_col = self.validate_row(board_transpose[row])
            if not valid_col:
                return False
                
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                valid_square = self.validate_row(square)
                if not valid_square:
                    return False
        return True
    
    
    def validate_row(self, test_row: List[str]):
        curr = ''
        for char in test_row:
            if char == '.':
                continue
            elif char not in curr:
                curr += char
            else:
                return False
        return True
        
        
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        big = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in big or (cur,j) in big or (i//3,j//3,cur) in big:
                        return False
                    big.add((i,cur))
                    big.add((cur,j))
                    big.add((i//3,j//3,cur))
        return True
