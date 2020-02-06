class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        nrow = len(board)
        ncol = len(board[0])
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        elif board[click[0]][click[1]]== "E":
            count = 0
            for neighbor in [[click[0] - 1, click[1] - 1], [click[0] - 1, click[1]], [click[0] - 1, click[1] + 1], [click[0] + 1, click[1] - 1], [click[0] + 1, click[1]], [click[0], click[1] - 1], [click[0], click[1] + 1], [click[0] + 1, click[1] + 1]]:
                if neighbor[0] >= 0 and neighbor[0] < nrow and neighbor[1] >= 0 and neighbor[1] < ncol:
                    if board[neighbor[0]][neighbor[1]] == "M":
                        count += 1
            if count:
                board[click[0]][click[1]] = str(count)
            else:
                board[click[0]][click[1]] = "B"
                for neighbor in [[click[0] - 1, click[1] - 1], [click[0] - 1, click[1]], [click[0] - 1, click[1] + 1], [click[0] + 1, click[1] - 1], [click[0] + 1, click[1]], [click[0], click[1] - 1], [click[0], click[1] + 1], [click[0] + 1, click[1] + 1]]:
                    if neighbor[0] >= 0 and neighbor[0] < nrow and neighbor[1] >= 0 and neighbor[1] < ncol:
                        self.updateBoard(board, neighbor)
        return board