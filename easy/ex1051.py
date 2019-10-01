class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = heights.copy()
        heights.sort()
        self.ans = 0
        for i in range(len(heights)):
            if heights[i] != temp[i]:
                self.ans += 1
        return self.ans
