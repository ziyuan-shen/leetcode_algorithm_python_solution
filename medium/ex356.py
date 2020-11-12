class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points = list(set([(p[0], p[1]) for p in points]))
        points.sort()
        if len(points) % 2 == 0:
            left = points[:len(points) // 2]
            right = points[len(points) // 2:]
            right.sort(key = lambda x: (x[0], -x[1]))
            xtotal = left[-1][0] + right[0][0]
        else:
            left = points[:len(points) // 2]
            right = points[len(points) // 2 + 1:]
            xtotal = 2 * points[len(points) // 2][0]
        while left and right and left[-1][0] == xtotal / 2 and right[0][0] == xtotal / 2:
            left.pop()
            right.pop(0)
        for i in range(len(left)):
            if right[i][1] != left[-(i+1)][1]:
                return False
            if right[i][0] + left[-(i+1)][0] != xtotal:
                return False
        return True
        