class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = str(N)
        if len(s) == 1:
            return N
        idx = 1
        while idx < len(s) and s[idx] >= s[idx-1]:
            idx += 1
        if idx == len(s):
            return N
        idx -= 1
        while idx >= 1 and s[idx] == s[idx-1]:
            idx -= 1
        return int(s[:idx] + str(int(s[idx]) - 1) + '9' * (len(s) - idx - 1))