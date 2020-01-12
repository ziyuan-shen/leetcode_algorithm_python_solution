class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = 1 if player == 1 else -1
        rowsum = sum(self.board[row])
        colsum = sum([self.board[r][col] for r in range(self.n)])
        diagsum1 = sum([self.board[i][i] for i in range(self.n)])
        diagsum2 = sum([self.board[i][-i-1] for i in range(self.n)])
        if player == 1:
            if rowsum == self.n or colsum == self.n or diagsum1 == self.n or diagsum2 == self.n:
                return 1
        else:
            if rowsum == -self.n or colsum == -self.n or diagsum1 == -self.n or diagsum2 == -self.n:
                return 2
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)