class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == []:
            return False
        nrow = len(board)
        ncol = len(board[0])
        for i in range(nrow):
            for j in range(ncol):
                if self.dfs(board, i, j, 0, word):
                    return True
        return False
    
    def dfs(self, board, i, j, idx, word):
        if idx == len(word):
            return True
        else:
            nrow = len(board)
            ncol = len(board[0])
            if i >= 0 and i < nrow and j >= 0 and j < ncol and board[i][j] == word[idx]:
                original = board[i][j]
                board[i][j] = ""
                if self.dfs(board, i-1, j, idx+1, word) or self.dfs(board, i+1, j, idx+1, word) or self.dfs(board, i, j-1, idx+1, word) or self.dfs(board, i, j+1, idx+1, word):
                    return True
                board[i][j] = original
                return False
            else:
                return False