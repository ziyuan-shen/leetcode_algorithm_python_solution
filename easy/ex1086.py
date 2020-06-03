from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for item in items:
            scores[item[0]].append(item[1])
        ans = {}
        for student in scores:
            scores[student].sort(reverse=True)
            ans[student] = sum(scores[student][:5]) // 5
        ans = [[key, value] for key, value in ans.items()]
        ans.sort()
        return ans