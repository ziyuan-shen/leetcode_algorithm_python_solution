from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""
        countdic = Counter(S)
        counttuple = [(countdic[letter], letter) for letter in countdic.keys()]
        if len(counttuple) == 1:
            return S if len(S) == 1 else ""
        counttuple.sort(reverse = True)
        counts = [x[0] for x in counttuple]
        topcount = counts[0]
        if topcount > sum(counts[1:]) + 1:
            return ""
        letters = [x[1] for x in counttuple]
        topletter = letters[0]
        ans = [topletter for _ in range(topcount)]
        rem = ""
        for i in range(1, len(counttuple)):
            rem += letters[i] * counts[i]
        idx = 0
        while idx < len(rem):
            for i in range(len(ans)):
                ans[i] += rem[idx]
                idx += 1
                if idx >= len(rem):
                    break
        return "".join(ans)