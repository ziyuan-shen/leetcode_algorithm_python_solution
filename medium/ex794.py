class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xcount = 0
        ocount = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    xcount += 1
                if board[i][j] == "O":
                    ocount += 1
        if xcount < ocount or ocount < xcount - 1:
            return False
        line1, line2 = 0, 0
        for i in range(3):
            if board[i] == "XXX":
                line1 += 1
            if board[i] == "OOO":
                line2 += 1
            if board[0][i] + board[1][i] + board[2][i] == "XXX":
                line1 += 1
            if board[0][i] + board[1][i] + board[2][i] == "OOO":
                line2 += 1
        if board[0][0] + board[1][1] + board[2][2] == "XXX":
            line1 += 1
        if board[0][0] + board[1][1] + board[2][2] == "OOO":
            line2 += 1
        if board[0][2] + board[1][1] + board[2][0] == "XXX":
            line1 += 1
        if board[0][2] + board[1][1] + board[2][0] == "OOO":
            line2 += 1
        if line1 >= 1 and line2 >= 1:
            return False
        if line1 >= 1 and ocount >= xcount:
            return False
        if line2 >= 1 and xcount > ocount:
            return False
        return True