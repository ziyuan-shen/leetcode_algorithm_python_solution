class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left_high = [0 for _ in range(len(height))]
        right_high = [0 for _ in range(len(height))]
        left_high[0] = height[0]
        for i in range(1, len(height)):
            left_high[i] = max(height[i], left_high[i-1])
        right_high[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_high[i] = max(height[i], right_high[i+1])
        ans = 0
        for i in range(1, len(height) - 1):
            low = min(left_high[i-1], right_high[i+1])
            if height[i] < low:
                ans += (low - height[i])
        return ans