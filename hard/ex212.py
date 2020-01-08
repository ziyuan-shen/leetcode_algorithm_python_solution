import copy
class Solution:
    def findword(self, i, j, board, word, idx):
        if idx == len(word):
            return True
        if i < 0 or i >= self.nrow or j < 0 or j >= self.ncol or board[i][j] != word[idx]:
            return False
        board[i][j] = ""
        for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if self.findword(r, c, board, word, idx + 1):
                return True
        board[i][j] = word[idx]
        return False
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        ans = []
        self.nrow = len(board)
        self.ncol = len(board[0])
        for word in words:
            boardcopy = copy.deepcopy(board)
            flag = False
            for i in range(self.nrow):
                for j in range(self.ncol):
                    if self.findword(i, j, boardcopy, word, 0):
                        ans.append(word)
                        flag = True
                        break
                if flag:
                    break
        return ans