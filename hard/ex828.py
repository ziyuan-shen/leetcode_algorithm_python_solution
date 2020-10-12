class Solution:
    def uniqueLetterString(self, s: str) -> int:
        if not s:
            return 0
        # sum of countUniqueChars for substrings end in s[i]
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        seen = {s[0]: [0]}
        for i in range(1, len(s)):
            if s[i] not in seen:
                dp[i] =  1 + dp[i-1] + i
                seen[s[i]] = [i]
            else:
                if len(seen[s[i]]) == 1:
                    dp[i] = 1 + dp[i-1] + (i - seen[s[i]][0] - 1) - (seen[s[i]][0] + 1)
                else:
                    dp[i] = 1 + dp[i-1] + (i - seen[s[i]][-1] - 1) - (seen[s[i]][-1] - seen[s[i]][-2])
                seen[s[i]].append(i)
        return sum(dp)