class Solution:        
    def numDupDigitsAtMostN(self, N: int) -> int:
        if N < 11:
            return 0
        length = len(str(N))
        fac = [1 for _ in range(10)]
        for i in range(2, 10):
            fac[i] = fac[i-1] * i
        ans = 0
        for l in range(2, length):
            ans += (9 * 10 ** (l - 1) - (9 * fac[9] // fac[10 - l]) if l <= 10 else 0)
        digits = [int(num) for num in str(N)]
        hasRepeated = [False for _ in range(len(digits))]
        seen = {digits[0]}
        for i in range(1, len(digits)):
            if hasRepeated[i-1]:
                hasRepeated[i] = True
            elif digits[i] in seen:
                hasRepeated[i] = True
            else:
                seen.add(digits[i])
        if digits[0] > 1:
            ans += ((digits[0] - 1) * (10 ** (len(digits) - 1) - (fac[9] // fac[10 - length]) if length <= 10 else 0))
        if hasRepeated[-2]:
            ans += digits[-1] + 1
        else:
            for num in range(digits[-1] + 1):
                if num in set(digits[:-1]):
                    ans += 1
        for i in range(1, length - 1):
            if hasRepeated[i-1]:
                ans += digits[i] * (10 ** (length - i - 1))
            else:
                for num in range(digits[i]):
                    if num in set(digits[:i]):
                        ans += 10 ** (length - i - 1)
                    else:
                        ans += (10 ** (length - i - 1) - (fac[9 - i] // fac[10 - length]) if length <= 10 else 0)
        return ans