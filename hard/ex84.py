class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areas = [0 for _ in range(len(heights))]
        ans = 0
        for i in range(len(heights)):
            height_min = heights[i]
            area_max = height_min
            for j in range(i+1, len(heights)):
                height_min = min(height_min, heights[j])
                area_max = max(area_max, (j - i + 1) * height_min)
            ans = max(ans, area_max)
        return ans