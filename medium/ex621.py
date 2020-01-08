from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskdic = Counter(tasks)
        nums = list(taskdic.values())
        if n == 0:
            return sum(nums)
        nums.sort()
        q = [[1] for _ in range(nums[-1] - 1)]
        nums.pop()
        ans = len(q) * (n + 1) + 1
        while q and nums:
            num = nums.pop()
            if num > len(q):
                ans += num - len(q)
            for i in range(min(num, len(q))):
                q[len(q) - i - 1].append(1)
            q.sort(reverse = True)
            while q and len(q[0]) >= n + 1:
                q.pop(0)
        if nums:
            ans += sum(nums)
        return ans
                