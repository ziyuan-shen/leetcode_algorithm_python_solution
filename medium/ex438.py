from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pcount = Counter(p)
        scount = Counter(s[:len(p)])
        ans = []
        if pcount == scount:
            ans.append(0)
        for i in range(len(p), len(s)):
            j = i - len(p)
            if s[j] in scount:
                if scount[s[j]] == 1:
                    scount.pop(s[j])
                else:
                    scount[s[j]] -= 1
            if s[i] in scount:
                scount[s[i]] += 1
            else:
                scount[s[i]] = 1
            if scount == pcount:
                ans.append(j+1)
        return ans