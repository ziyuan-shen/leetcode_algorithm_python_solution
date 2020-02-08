class Solution:
    def crush(self, board):
        for r in range(self.nrow):
            p1 = 0
            p2 = 1
            while p2 < self.ncol - 1:
                val = abs(board[r][p1])
                while p2 < self.ncol and abs(board[r][p2]) == val:
                    p2 += 1
                if p2 - p1 > 2:
                    for c in range(p1, p2):
                        board[r][c] = -val
                p1 = p2
                p2 += 1
        for c in range(self.ncol):
            p1 = 0
            p2 = 1
            while p2 < self.nrow - 1:
                val = abs(board[p1][c])
                while p2 < self.nrow and abs(board[p2][c]) == val:
                    p2 += 1
                if p2 - p1 > 2:
                    for r in range(p1, p2):
                        board[r][c] = -val
                p1 = p2
                p2 += 1
        change_flag = False
        for r in range(self.nrow):
            for c in range(self.ncol):
                if board[r][c] < 0:
                    change_flag = True
                    board[r][c] = 0
        return change_flag
        
    def gravity(self, board):
        for c in range(self.ncol):
            p1 = self.nrow - 1
            p2 = p1 - 1
            while p2 >= 0:
                if board[p1][c] != 0:
                    p1 -= 1
                    p2 -= 1
                else:
                    while p2 >= 0 and board[p2][c] == 0:
                        p2 -= 1
                    if p2 >= 0:
                        board[p1][c] = board[p2][c]
                        board[p2][c] = 0
                    p1 -= 1
                    p2 = p1 - 1
        
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self.nrow = len(board)
        self.ncol = len(board[0])
        while self.crush(board):
            self.gravity(board)
        return board
        