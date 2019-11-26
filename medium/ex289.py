class Solution:
    def getNeighbourSum(self, i, j, board):
        nodes = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
        neighbour_sum = 0
        for node in nodes:
            x = node[0]
            y = node[1]
            if x>=0 and x<len(board) and y>=0 and y<len(board[0]):
                if board[x][y] == -1 or board[x][y] == 1:
                    neighbour_sum += 1
        return neighbour_sum
    
    def update_cell(self, cell, neighbour_sum):
        if cell==0:
            if neighbour_sum == 3:
                return 2
            else:
                return 0
        else:
            if neighbour_sum < 2 or neighbour_sum > 3:
                return -1
            else:
                return 1
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = self.update_cell(board[i][j], self.getNeighbourSum(i, j, board))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1