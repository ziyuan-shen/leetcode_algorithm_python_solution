class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        dp[-1] = s[-1] in wordDict
        for i in range(len(s)-2, -1, -1):
            idx = i
            while idx < len(s):
                if idx == len(s) - 1:
                    dp[i] = s[i:] in wordDict
                elif s[i:idx+1] in wordDict and dp[idx+1]:
                    dp[i] = True
                    break
                idx += 1
        return dp[0]