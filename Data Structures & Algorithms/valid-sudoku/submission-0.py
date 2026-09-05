class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # CHECK 1: every row
        for r in range(9):
            seen = []
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.append(val)
        
        # CHECK 2: every column
        for c in range(9):
            seen = []
            for r in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.append(val)
        
        # CHECK 3: every 3x3 box
        for box_row in range(3):
            for box_col in range(3):
                seen = []
                for r in range(box_row * 3, box_row * 3 + 3):
                    for c in range(box_col * 3, box_col * 3 + 3):
                        val = board[r][c]
                        if val == '.':
                            continue
                        if val in seen:
                            return False
                        seen.append(val)
        
        return True
        