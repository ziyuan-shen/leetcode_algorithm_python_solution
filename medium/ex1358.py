from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        p1 = 0
        dic = defaultdict(list)
        dic[s[0]].append(0)
        p2 = 1
        while p2 < len(s):
            while len(dic) < 3 and p2 < len(s):
                dic[s[p2]].append(p2)
                p2 += 1
            if len(dic) == 3:
                ans += len(s) - p2 + 1
                while p1 < len(s) and len(dic[s[p1]]) > 1:
                    dic[s[p1]].pop(0)
                    ans += len(s) - p2 + 1
                    p1 += 1
                if p1 < len(s):
                    dic.pop(s[p1])
                    p1 += 1
        return ans