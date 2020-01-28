class Solution:    
    def maxSum(self, A, L, M):
        ans = 0
        for i in range(len(A) - L - M + 1):
            suml = sum(A[i:i+L])
            for j in range(i+L, len(A) - M + 1):
                ans = max(ans, suml + sum(A[j:j+M]))
        return ans
        
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        return max(self.maxSum(A, L, M), self.maxSum(A, M, L))