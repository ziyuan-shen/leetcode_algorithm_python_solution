from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        seen = defaultdict(int)
        ans = []
        for i in range(len(s) - 9):
            if s[i:i+10] in seen:
                if seen[s[i:i+10]] == 1:
                    ans.append(s[i:i+10])
            seen[s[i:i+10]] += 1
        return ans