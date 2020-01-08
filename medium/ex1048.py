from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        worddic = defaultdict(set)
        for word in words:
            worddic[len(word)].add(word)
        lendic = {}
        for length in worddic:
            lendic[length] = {w: 1 for w in worddic[length]}
        for length in range(min(worddic) + 1, max(worddic) + 1):
            for w in worddic[length]:
                pathlens = [1]
                for m in range(length):
                    if w[:m] + w[m+1:] in worddic[length-1]:
                        pathlens.append(lendic[length-1][w[:m] + w[m+1:]] + 1)
                lendic[length][w] = max(pathlens)
        ans = 1
        for length in worddic:
            ans = max(ans, max(lendic[length].values()))
        return ans