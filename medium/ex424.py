from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        start, end = 0, 1
        counts = defaultdict(int)
        counts[s[start]] = 1
        ans = 1
        candidate_count = 1
        while end < len(s):
            counts[s[end]] += 1
            candidate_count = max(candidate_count, counts[s[end]])
            while end - start + 1 - candidate_count > k:
                counts[s[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)
            end += 1
        return ans
            