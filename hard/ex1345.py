from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        idxdic = defaultdict(list)
        for i in range(len(arr)):
            idxdic[arr[i]].append(i)
        q = deque([(len(arr) - 1, 0)])
        visited = {len(arr) - 1}
        while q:
            idx, level = q.popleft()
            if idx == 1:
                return level + 1
            for nei in idxdic[arr[idx]]:
                if nei == 0:
                    return level + 1
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, level + 1))
            if idx - 1 >= 0 and idx - 1 not in visited:
                visited.add(idx - 1)
                q.append((idx-1, level + 1))
            if idx + 1 < len(arr) and idx + 1 not in visited:
                visited.add(idx + 1)
                q.append((idx+1, level + 1))
        return -1