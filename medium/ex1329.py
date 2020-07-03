class Solution:
    def sortLines(self, start_node):
        line = [start_node]
        while True:
            next_row, next_col = line[-1][0] + 1, line[-1][1] + 1
            if next_row < self.length and next_col < self.width:
                line.append((next_row, next_col))
            else:
                break
        line_sorted = [self.mat[x][y] for x, y in line]
        line_sorted.sort()
        idx = 0
        for x, y in line:
            self.ans[x][y] = line_sorted[idx]
            idx += 1
            
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        self.length = len(mat)
        self.width = len(mat[0])
        self.mat = mat
        self.ans = [[0 for _ in range(self.width)] for _ in range(self.length)]
        for i in range(self.width - 1, -1, -1):
            self.sortLines((0, i))
        for i in range(1, self.length):
            self.sortLines((i, 0))
        return self.ans