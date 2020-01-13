from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        ans = [[count[key], key] for key in count]
        ans.sort(key = lambda x: (-x[0], x[1]))
        return [t[1] for t in ans][:k]