class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            filtered_row = [num for num in row if num != "."]
            if len(filtered_row) != len(set(filtered_row)):
                return False

        for column in zip(*board):
            filtered_column = [num for num in column if num != "."]
            if len(filtered_column) != len(set(filtered_column)):
                return False

        box = []

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)  

        return True
        



        