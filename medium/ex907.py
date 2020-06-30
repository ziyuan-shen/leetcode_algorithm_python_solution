class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        ans = 0
        dot = 0
        for j in range(len(A)):
            count = 0
            while stack and stack[-1][0] >= A[j]:
                val, c = stack.pop()
                dot -= val * c
                count += c
            stack.append((A[j], count + 1))
            dot += A[j] * (count + 1)
            ans += dot
        return ans % (10 ** 9 + 7)