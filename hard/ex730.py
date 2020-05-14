class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)]
        for i in range(n):
            dp[ord(S[i])-97][i][i] = 1
        for i in range(n-1):
            dp[ord(S[i])-97][i][i+1] = 1
            dp[ord(S[i+1])-97][i][i+1] = 1
            if S[i] == S[i+1]:
                dp[ord(S[i])-97][i][i+1] += 1
        for length in range(2, n):
            for i in range(n-length):
                for j in range(4):
                    if (ord(S[i])-97) != j:
                        dp[j][i][i+length] = dp[j][i+1][i+length]
                    elif (ord(S[i+length])-97) != j:
                        dp[j][i][i+length] = dp[j][i][i+length-1]
                    else:
                        dp[j][i][i+length] = dp[0][i+1][i+length-1] + dp[1][i+1][i+length-1] + dp[2][i+1][i+length-1] + dp[3][i+1][i+length-1] + 2
        return (dp[0][0][n-1]+dp[1][0][n-1]+dp[2][0][n-1]+dp[3][0][n-1]) % (10 ** 9 + 7)