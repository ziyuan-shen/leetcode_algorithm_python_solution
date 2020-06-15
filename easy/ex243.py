class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word1_indices = []
        word2_indices = []
        for idx, word in enumerate(words):
            if word == word1:
                word1_indices.append(idx)
            elif word == word2:
                word2_indices.append(idx)
        ans = float("inf")
        for idx1 in word1_indices:
            for idx2 in word2_indices:
                ans = min(ans, abs(idx1 - idx2))
        return ans