class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = [[point, point[0] ** 2 + point[1] ** 2] for point in points]
        distance = sorted(distance, key = lambda x: x[1])
        return [x[0] for x in distance[:K]]