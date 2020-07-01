class Solution:
    def fillSeats(self, seats, x, y):
        ans = 0
        for i in range(x, self.M):
            for j in range(self.N):
                if i == x and j < y:
                    continue
                if seats[i][j] == ".":
                    seats[i][j] = "#"
                    blocks = set()
                    if j + 1 < self.N and seats[i][j+1] == ".":
                        blocks.add((i, j+1))
                    if i + 1 < self.M and j - 1 >= 0 and seats[i+1][j-1] == ".":
                        blocks.add((i+1, j-1))
                    if i + 1 < self.M and j + 1 < self.N and seats[i+1][j+1] == ".":
                        blocks.add((i+1, j+1))
                    for block in blocks:
                        seats[block[0]][block[1]] = "#"
                    ans = max(ans, 1 + self.fillSeats(seats, i, j+1))
                    seats[i][j] = "."
                    for block in blocks:
                        seats[block[0]][block[1]] = "."
                    ans = max(ans, self.fillSeats(seats, i, j+1))
                    return ans
        return 0
    
    def maxStudents(self, seats: List[List[str]]) -> int:
        self.M = len(seats)
        self.N = len(seats[0])
        return self.fillSeats(seats, 0, 0)