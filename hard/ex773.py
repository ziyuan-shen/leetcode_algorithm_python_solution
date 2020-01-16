from itertools import permutations
from collections import defaultdict
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        idxdic = {t: idx for idx, t in enumerate(permutations(range(6)))}
        neighbordic = {0: {1, 3}, 1: {0, 2, 4}, 2: {1, 5}, 3: {0, 4}, 4: {1, 3, 5}, 5: {2, 4}}
        edgedic = defaultdict(set)
        for t in idxdic:
            idx = t.index(0)
            for neighbor in neighbordic[idx]:
                switch_idx1 = min(idx, neighbor)
                switch_idx2 = max(idx, neighbor)
                edgedic[idxdic[t]].add(idxdic[t[:switch_idx1] + (t[switch_idx2],) + t[switch_idx1+1:switch_idx2] + (t[switch_idx1],) + t[switch_idx2+1:]])
        q = deque([])
        start = idxdic[tuple(board[0] + board[1])]
        end = idxdic[(1,2,3,4,5,0)]
        if start == end:
            return 0
        q.append((start, 0))
        visited = {i: False for i in idxdic.values()}
        visited[start] = True
        while q:
            node, level = q.popleft()
            for neighbor in edgedic[node]:
                if not visited[neighbor]:
                    if neighbor == end:
                        return level + 1
                    visited[neighbor] = True
                    q.append((neighbor, level + 1))
        return -1