def find_box_coords(r, c):
    sr, sc, er, ec = 0, 0, 0, 0

    if r <= 2:
        sr = 0
        er = 2
    elif r > 2 and r <= 5:
        sr = 3
        er = 5
    else:
        sr = 6
        er = 8
        
    if c <= 2:
        sc = 0
        ec = 2
    elif c > 2 and c <= 5:
        sc = 3
        ec = 5
    else:
        sc = 6
        ec = 8
    
    return (sr, sc, er, ec)

    
# Requires that board[r][c] != .
def validate_filled(r, c, board):
    # Check rows
    for _r, row in enumerate(board):
        if _r != r and row[c] == board[r][c]: return False
    
    # Check cols
    for _c, col in enumerate(board[r]):
        if _c != c and col == board[r][c]: return False
    
    # Check box
    sr, sc, er, ec = find_box_coords(r, c)
    print((sr, sc, er, ec))
    for _r in range(sr, er + 1):
        for _c in range(sc, ec + 1):    
            if _r != r and _c != c and board[_r][_c] == board[r][c]: return False
    
    return True

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] != "." and not validate_filled(r, c, board):
                    return False
        
        return True