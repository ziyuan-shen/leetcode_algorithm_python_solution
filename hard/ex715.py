from bisect import bisect_left, bisect_right
class RangeModule:

    def __init__(self):
        self.ranges = []
        
    def _bounds(self, left, right):
        i = bisect_right([r[0] for r in self.ranges], left) - 1
        j = bisect_left([r[1] for r in self.ranges], right)
        return i, j

    def addRange(self, left: int, right: int) -> None:
        if not self.ranges:
            self.ranges.append([left, right])
        i, j = self._bounds(left, right)
        if i == j:
            return
        if i == -1 and j == len(self.ranges):
            self.ranges = [[left, right]]
        elif i == -1:
            if self.ranges[j][0] > right:
                self.ranges[:j] = [[left, right]]
            else:
                self.ranges[:j+1] = [[left, self.ranges[j][1]]]
        elif j == len(self.ranges):
            if self.ranges[i][1] < left:
                self.ranges[i+1:] = [[left, right]]
            else:
                self.ranges[i:] = [[self.ranges[i][0], right]]
        else:
            if left <= self.ranges[i][1]:
                if right < self.ranges[j][0]:
                    self.ranges[i:j] = [[self.ranges[i][0], right]]
                else:
                    self.ranges[i:j+1] = [[self.ranges[i][0], self.ranges[j][1]]]
            else:
                if right < self.ranges[j][0]:
                    self.ranges[i+1:j] = [[left, right]]
                else:
                    self.ranges[i+1:j+1] = [[left, self.ranges[j][1]]]

    def queryRange(self, left: int, right: int) -> bool:
        i, j = self._bounds(left, right)
        return i != -1 and j != len(self.ranges) and i == j

    def removeRange(self, left: int, right: int) -> None:
        if not self.ranges:
            return
        i, j = self._bounds(left, right)
        if i == j:
            l, r = self.ranges[i][0], self.ranges[i][1]
            if l == left and r == right:
                del self.ranges[i]
            elif l == left:
                self.ranges[i][0] = right
            elif r == right:
                self.ranges[i][1] = left
            else:
                self.ranges[i][1] = left
                self.ranges.insert(i+1, [right, r])
            return
        if i == -1 and j == len(self.ranges):
            self.ranges = []
        elif i == -1:
            if self.ranges[j][0] <= right:
                self.ranges[j][0] = right
            del self.ranges[:j]
        elif j == len(self.ranges):
            if self.ranges[i][1] >= left:
                self.ranges[i][1] = left
            del self.ranges[i+1:]
        else:
            if left <= self.ranges[i][1]:
                self.ranges[i][1] = left
            if right > self.ranges[j][0]:
                self.ranges[j][0] = right
            del self.ranges[i+1:j]
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)