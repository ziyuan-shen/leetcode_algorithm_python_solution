class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        m = bin(m)[2:]
        n = bin(n)[2:]
        if len(m) != len(n):
            return 0
        idx = 0
        while idx < len(m):
            if m[idx] == n[idx]:
                idx += 1
            else:
                break
        return int(m[:idx] + "0" * (len(m) - idx), 2)