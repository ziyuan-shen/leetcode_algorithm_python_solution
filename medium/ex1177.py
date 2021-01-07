from collections import Counter
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 0
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                dp[i][i+1] = 1
        for i in range(len(s) - 2):
            d = Counter(s[i:i+3])
            oddnum = 0
            for value in d.values():
                if value % 2 == 1:
                    oddnum += 1
            dp[i][i+2] = (oddnum - 1) // 2
            for j in range(i+3, len(s)):
                if s[j] in d:
                    d[s[j]] += 1
                    if d[s[j]] % 2 == 1:
                        oddnum += 1
                    else:
                        oddnum -= 1
                else:
                    oddnum += 1
                    d[s[j]] = 1
                dp[i][j] = (oddnum - ((j-i+1) % 2)) // 2
        ans = [False for _ in range(len(queries))]
        for idx, q in enumerate(queries):
            if dp[q[0]][q[1]] <= q[2]:
                ans[idx] = True
        return ans