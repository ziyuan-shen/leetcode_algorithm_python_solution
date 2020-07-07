class Solution:
    def dfs(self, node, board, border_connections):
        border_connections.add(node)
        for neighbor in [(node[0] + 1, node[1]), (node[0] - 1, node[1]), (node[0], node[1] + 1), (node[0], node[1] -1)]:
            if neighbor[0] >= 0 and neighbor[0] < self.length and neighbor[1] >= 0 and neighbor[1] < self.width:
                if neighbor not in border_connections and board[neighbor[0]][neighbor[1]] == "O":
                    self.dfs(neighbor, board, border_connections)
                    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        border_connections = set()
        self.length = len(board)
        self.width = len(board[0])
        for i in [0, self.length - 1]:
            for j in range(self.width):
                if board[i][j] == "O" and (i, j) not in border_connections:
                    self.dfs((i, j), board, border_connections)
        for j in [0, self.width - 1]:
            for i in range(self.length):
                if board[i][j] == "O" and (i, j) not in border_connections:
                    self.dfs((i, j), board, border_connections)
        for i in range(1, self.length-1):
            for j in range(1, self.width-1):
                if board[i][j] == "O" and (i, j) not in border_connections:
                    board[i][j] = "X"