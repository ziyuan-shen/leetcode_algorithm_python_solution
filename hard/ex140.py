from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        dp = defaultdict(set)
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    if j == len(s) - 1:
                        dp[i].add(s[i:j+1])
                    for sentence in dp[j+1]:
                        dp[i].add(s[i:j+1] + " " + sentence)
        return list(dp[0])