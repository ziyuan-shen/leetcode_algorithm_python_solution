from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        q = deque([[num] for num in candidates])
        ans = []
        if [target] in q:
            ans.append([target])
        while q:
            possible = q.popleft()
            diff = target - sum(possible)
            idx = candidates.index(possible[-1])
            for num in candidates[idx:]:
                if num < diff:
                    q.append(possible + [num])
                elif num == diff:
                    ans.append(possible + [num])
                else:
                    break
        return ans