class Solution:
    def getNeighbors(self, a, b):
        if a == self.x and b == self.y:
            return [(a, 0), (0, b)]
        elif a == self.x and b == 0:
            if self.x <= self.y:
                return [(0, a)]
            else:
                return [(a - self.y, self.y)]
        elif a == 0 and b == self.y:
            if self.x >= self.y:
                return [(b, 0)]
            else:
                return [(self.x, b - self.x)]
        elif a == self.x and b != 0:
            neighbors = [(0, b)]
            if a <= self.y - b:
                neighbors.append((0, a+b))
            else:
                neighbors.append((a+b-self.y, self.y))
        elif a == 0 and b != self.y:
            neighbors = [(self.x, b)]
            if b <= self.x:
                neighbors.append((b, 0))
            else:
                neighbors.append((self.x, b-self.x))
        elif a != self.x and b == 0:
            neighbors = [(a, self.y)]
            if a <= self.y:
                neighbors.append((0, a))
            else:
                neighbors.append((a-self.y, self.y))
        else:
            neighbors = [(a, 0)]
            if b <= self.x - a:
                neighbors.append((a+b, 0))
            else:
                neighbors.append((self.x, a+b-self.x))
        return neighbors
        
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        self.x = x
        self.y = y
        q = [(x, y)]
        visited = {(x, y)}
        if x == z or y == z or (x + y) == z:
            return True
        while q:
            a, b = q.pop(0)
            for neighbor in self.getNeighbors(a, b):
                if neighbor not in visited:
                    if neighbor[0] == z or neighbor[1] == z or (neighbor[0] + neighbor[1]) == z:
                        return True
                    visited.add(neighbor)
                    q.append(neighbor)
        return False