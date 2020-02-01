from collections import deque
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        ans = [-1 for _ in range(len(workers))]
        distances = deque([])
        for wi, worker in enumerate(workers):
            for bi, bike in enumerate(bikes):
                distances.append((abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]), wi, bi))
        distances = deque(sorted(list(distances)))
        added_worker = set()
        added_bike = set()
        while len(added_worker) < len(workers):
            distance, wi, bi = distances.popleft()
            if wi in added_worker:
                continue
            if bi in added_bike:
                continue
            added_worker.add(wi)
            added_bike.add(bi)
            ans[wi] = bi
        return ans