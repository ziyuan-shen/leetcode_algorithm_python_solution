from collections import Counter
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        oddletters = [None for _ in range(len(s) + 1)]
        oddletters[0] = set()
        for i in range(1, len(s) + 1):
            oddletters[i] = oddletters[i-1].copy()
            if s[i-1] in oddletters[i-1]:
                oddletters[i].remove(s[i-1])
            else:
                oddletters[i].add(s[i-1])
        ans = [False for _ in range(len(queries))]
        for idx, q in enumerate(queries):
            s1 = oddletters[q[0]]
            s2 = oddletters[q[1] + 1]
            if (len(s1) + len(s2) - 2 * len(s1.intersection(s2)) - ((q[1] - q[0] + 1) % 2)) // 2 <= q[2]:
                ans[idx] = True
        return ans