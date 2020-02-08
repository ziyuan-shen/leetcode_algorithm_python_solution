from collections import defaultdict
class WordDistance:

    def __init__(self, words: List[str]):
        self.map = defaultdict(list)
        for idx, word in enumerate(words):
            self.map[word].append(idx)
        
    def shortest(self, word1: str, word2: str) -> int:
        idx1 = self.map[word1]
        idx2 = self.map[word2]
        p1 = 0
        p2 = 0
        ans = float("inf")
        while p1 < len(idx1) and p2 < len(idx2):
            if idx1[p1] == idx2[p2]:
                return 0
            else:
                ans = min(ans, abs(idx1[p1] - idx2[p2]))
                if idx1[p1] < idx2[p2]:
                    p1 += 1
                else:
                    p2 += 1
        return ans

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)