class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        for p1 in range(len(s)-2):
            p2 = p1
            seen = set(s[p1])
            while len(seen) < 3 and p2 < len(s) - 1:
                p2 += 1
                seen.add(s[p2])
            if len(seen) == 3:
                ans += len(s) - p2
        return ans