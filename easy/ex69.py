class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 2:
            return 1
        low = 1
        high = x // 2
        while True:
            mid = (low + high) // 2
            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid - 1