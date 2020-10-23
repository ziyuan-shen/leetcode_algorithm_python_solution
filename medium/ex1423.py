class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        if k == len(cardPoints):
            return total
        sub = sum(cardPoints[:len(cardPoints) - k])
        current = sub
        for i in range(len(cardPoints) - k, len(cardPoints)):
            current -= cardPoints[i - len(cardPoints) + k]
            current += cardPoints[i]
            sub = min(sub, current)
        return total - sub