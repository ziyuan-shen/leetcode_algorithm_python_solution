class Solution:
    def binaryCheck(self, N, x, low, high):
        while low <= high:
            mid = (low + high) // 2
            target = (2 * x + mid - 1) * mid / 2
            if target == N:
                return True
            if target < N:
                low = mid + 1
            else:
                high = mid - 1
        return False
        
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        for x in range(1, N+1):
            if self.binaryCheck(N, x, 1, N - x + 1):
                ans += 1
        return ans