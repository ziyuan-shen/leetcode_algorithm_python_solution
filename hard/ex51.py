from collections import defaultdict
class Solution:
    def could_place(self, row, col):
        return (not self.attacked_cols[col]) and (not self.attacked_diag1[row + col]) and (not self.attacked_diag2[row - col])
        
    def place(self, row, col):
        self.placed_cols[row] = col
        self.attacked_cols[col] = True
        self.attacked_diag1[row + col] = True
        self.attacked_diag2[row - col] = True
        
    def remove(self, row, col):
        self.placed_cols[row] = -1
        self.attacked_cols[col] = False
        self.attacked_diag1[row + col] = False
        self.attacked_diag2[row - col] = False
        
    def back_track(self, row):
        for col in range(self.n):
            if self.could_place(row, col):
                self.place(row, col)
                if row == self.n - 1:
                    self.ans.append(["." * self.placed_cols[i] + "Q" + "." * (self.n - 1 - self.placed_cols[i]) for i in range(self.n)])
                else:
                    self.back_track(row + 1)
                self.remove(row, col)
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.attacked_cols = defaultdict(bool)
        self.attacked_diag1 = defaultdict(bool)
        self.attacked_diag2 = defaultdict(bool)
        self.ans = []
        self.placed_cols = [-1 for _ in range(n)]
        self.back_track(0)
        return self.ans
        
        