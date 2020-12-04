class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [dict() for _ in range(len(A))]
        ans = 1
        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A) - 1, i, -1):
                diff = A[j] - A[i]
                if diff in dp[j]:
                    dp[i][diff] = 1 + dp[j][diff]
                else:
                    dp[i][diff] = 2
                ans = max(ans, dp[i][diff])
        return ans