class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maxarea = min(height[0], height[-1]) * p2
        while (p2 - p1) > 1:
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
            newarea = min(height[p1], height[p2]) * (p2 - p1)
            if newarea > maxarea:
                maxarea = newarea
        return maxarea