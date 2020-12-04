class Solution:
    def bestlowpoint(self, x, y, dungeon):
        if (x, y) in self.mem:
            return self.mem[(x, y)]
        if x == len(dungeon) - 1 and y == len(dungeon[0]) - 1:
            self.mem[(x, y)] = dungeon[x][y]
            return self.mem[(x, y)]
        elif x < len(dungeon) - 1 and y == len(dungeon[0]) - 1:
            self.mem[(x, y)] = min(dungeon[x][y], dungeon[x][y] + self.bestlowpoint(x+1, y, dungeon))
            return self.mem[(x, y)]
        elif x == len(dungeon) - 1 and y < len(dungeon[0]) - 1:
            self.mem[(x, y)] = min(dungeon[x][y], dungeon[x][y] + self.bestlowpoint(x, y+1, dungeon))
            return self.mem[(x, y)]
        else:
            self.mem[(x, y)] = min(dungeon[x][y], dungeon[x][y] + max(self.bestlowpoint(x+1, y, dungeon), self.bestlowpoint(x, y+1, dungeon)))
            return self.mem[(x, y)]
        
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.mem = {}
        ans = self.bestlowpoint(0, 0, dungeon)
        return 1 if ans > 0 else 1 - ans