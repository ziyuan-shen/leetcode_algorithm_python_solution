class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        height = horizontalCuts[0]
        width = verticalCuts[0]
        for i in range(1, len(horizontalCuts)):
            height = max(height, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            width = max(width, verticalCuts[i] - verticalCuts[i-1])
        return (height * width) % (10 ** 9 + 7)