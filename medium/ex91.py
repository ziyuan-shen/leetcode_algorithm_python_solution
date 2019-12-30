class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if '1' <= s[0] <= '9' else 0
        
        for i in range(2, len(dp)):
            
            if '1' <= s[i - 1] <= '9':
                dp[i] += dp[i - 1]
                
            if '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]
        
        return dp[-1]