class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0:
                pattern = s[:i]
                flag = True
                for start in range(i, len(s), i):
                    if s[start:start + i] != pattern:
                        flag = False
                        break
                if flag:
                    return True
        return False