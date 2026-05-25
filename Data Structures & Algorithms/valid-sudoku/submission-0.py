class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen1 = set()
            for j in range(9):
                if (cell := board[i][j]) in seen1 and cell != ".":
                    return False
                seen1.add(cell)

            seen2 = set()
            for k in range(9):
                if (cell := board[k][i]) in seen2 and cell != ".":
                    return False
                seen2.add(cell)
        
        for start_i in range(0, 9, 3):
            for start_j in range(0, 9, 3):
                seen = set()
                for di in range(3):
                    for dj in range(3):
                        if (cell := board[start_i + di][start_j + dj]) in seen and cell != ".":
                            return False
                        seen.add(cell)
        return True        