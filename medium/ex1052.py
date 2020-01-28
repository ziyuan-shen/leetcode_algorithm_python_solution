class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        length = len(customers)
        filtered = [customers[i] if grumpy[i]==0 else 0 for i in range(length)]
        cumsum_left = [filtered[i] for i in range(length)]
        for i in range(1, length):
            cumsum_left[i] = cumsum_left[i-1] + filtered[i]
        cumsum_right = [filtered[i] for i in range(length)]
        for i in range(length-2, -1, -1):
            cumsum_right[i] = cumsum_right[i+1] + filtered[i]
        ans = 0
        for i in range(length - X + 1):
            ans = max(ans, (cumsum_left[i-1] if i > 0 else 0) + sum(customers[i:i+X]) + (cumsum_right[i+X] if i + X < length else 0))
        return ans