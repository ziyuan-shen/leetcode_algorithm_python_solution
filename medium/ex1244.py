from bisect import bisect
class Leaderboard:

    def __init__(self):
        self.idxdic = dict()
        self.scores = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.idxdic:
            idx = self.idxdic[playerId]
            score += self.scores[idx]
            del self.scores[idx]
            for player in self.idxdic:
                if self.idxdic[player] > idx:
                    self.idxdic[player] -= 1
        idx = bisect(self.scores, score)
        for player in self.idxdic:
            if self.idxdic[player] >= idx:
                self.idxdic[player] += 1
        self.idxdic[playerId] = idx
        self.scores.insert(idx, score)

    def top(self, K: int) -> int:
        return sum(self.scores[-K:])

    def reset(self, playerId: int) -> None:
        idx = self.idxdic[playerId]
        del self.scores[idx]
        self.idxdic.pop(playerId)
        for player in self.idxdic:
            if self.idxdic[player] > idx:
                self.idxdic[player] -= 1

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)