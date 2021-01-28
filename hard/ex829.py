class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        i = 1
        while i * (i - 1) < 2 * N:
            if 2 * N / i == 2 * N // i:
                if (2 * N // i + 1 - i) % 2 == 0:
                    ans += 1
            i += 1
        return ans