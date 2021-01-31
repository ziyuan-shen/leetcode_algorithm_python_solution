from collections import Counter
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teamnum = len(votes[0])
        scores = {team: [0 for _ in range(teamnum)] for team in votes[0]}
        for i in range(teamnum):
            for team, count in Counter([vote[i] for vote in votes]).items():
                scores[team][i] = -count
        scores = [score + [team] for team, score in scores.items()]
        scores.sort()
        return "".join([score[-1] for score in scores])