class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        length = len(board)
        width = len(board[0])
        for i in range(length):
            for j in range(width):
                if board[i][j] == "X":
                    ans += 1
                    for k in range(j+1, width):
                        if board[i][k] == "X":
                            board[i][k] = -1
                        else:
                            break
                    for k in range(i+1, length):
                        if board[k][j] == "X":
                            board[k][j] = -1
                        else:
                            break
        return ans