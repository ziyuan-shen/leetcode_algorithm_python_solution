from bisect import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.snapid = -1
        self.data = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.data[index][-1][0] == self.snapid + 1:
            self.data[index][-1][1] = val
        else:
            self.data[index].append([self.snapid+1, val])

    def snap(self) -> int:
        self.snapid += 1
        return self.snapid

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect(self.data[index], [snap_id, float("inf")])
        return self.data[index][idx-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)