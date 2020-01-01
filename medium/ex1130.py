class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        length = len(arr)
        dp = [[0 for _ in range(length + 1 - i)] for i in range(1, length+1)]
        for i in range(1, length):
            for j in range(length-i):
                dp[i][j] = min([max(arr[j:j+k+1]) * max(arr[j+k+1:j+i+1]) + dp[k][j] + dp[i-k-1][j+k+1] for k in range(i)])
        return dp[-1][-1]