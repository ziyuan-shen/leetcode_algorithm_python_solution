from collections import defaultdict
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        onboard = 0
        offboard = 0
        positions = {(r, c): 1}
        for i in range(K):
            new_positions = defaultdict(int)
            for p in positions:
                if p[0] >= 0 and p[0] < N and p[1] >= 0 and p[1] < N:
                    for nei in [(p[0]-2, p[1]+1), (p[0]-1, p[1]+2), (p[0]+1, p[1]+2), (p[0]+2, p[1]+1), (p[0]+2, p[1]-1), (p[0]+1, p[1]-2), (p[0]-1, p[1]-2), (p[0]-2, p[1]-1)]:
                        new_positions[nei] += positions[p]
                else:
                    offboard += positions[p] * 8 ** (K - i)
            positions = new_positions
        for p in positions:
            if p[0] >= 0 and p[0] < N and p[1] >= 0 and p[1] < N:
                onboard += positions[p]
            else:
                offboard += positions[p]
        return onboard / (onboard + offboard)