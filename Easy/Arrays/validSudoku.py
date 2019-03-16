
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    
    alreadyInRow = [[False] * 9 for _ in range(9)]
    alreadyInCol = [[False] * 9 for _ in range(9)]
    alreadyInSquare = [[False] * 9 for _ in range(9)] 

    for i in range(9):
        for j in range(9):
            if board[i][j] == "." : continue
            index = int(board[i][j]) -1 
            sq_index = i//3 *3 + j//3 
            if alreadyInRow[i][index] or alreadyInCol[j][index] or alreadyInSquare[sq_index][index] : 
                return False
            alreadyInRow[i][index] = alreadyInCol[j][index] = alreadyInSquare[sq_index][index] = True
    return True

def getSubSquare(m, i):
    subrow = (i // 3) * 3
    subcol = (i % 3) * 3
    v = [0] * 9
    for j in range(9):
        subrj = j // 3
        subcj = j % 3
        v[j] = m[subrow + subrj][subcol + subcj]
    return v

def getRow(m,i):
    return m[i]

def getCol(m,i):
    return [m[j][i] for j in range(9)]       

input1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","5","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(input1))

