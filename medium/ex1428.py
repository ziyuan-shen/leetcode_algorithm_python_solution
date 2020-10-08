# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        rows = dim[0]
        cols = dim[1]
        high = cols
        for r in range(rows):
            if high == 0:
                return 0
            if binaryMatrix.get(r, high - 1) == 0:
                continue
            l, h = 0, high - 1
            while l <= h:
                mid = (l + h) // 2
                if binaryMatrix.get(r, mid) == 0:
                    if mid + 1 == high or binaryMatrix.get(r, mid + 1) == 1:
                        high = mid + 1
                        break
                    else:
                        l = mid + 1
                else:
                    if mid == 0 or binaryMatrix.get(r, mid - 1) == 0:
                        high = mid
                        break
                    else:
                        h = mid - 1
        if high == cols:
            return -1
        else:
            return high