class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        for _ in range(V):
            minidx = K
            for i in range(K-1, -1, -1):
                if heights[i] > heights[i+1]:
                    break
                if heights[i] < heights[minidx]:
                    minidx = i
            if minidx == K:
                for i in range(K+1, len(heights)):
                    if heights[i] > heights[i-1]:
                        break
                    if heights[i] < heights[minidx]:
                        minidx = i
            heights[minidx] += 1
        return heights