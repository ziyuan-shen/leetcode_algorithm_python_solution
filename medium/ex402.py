from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        q = deque([0])
        for i in range(1, k + 1):
            while q and num[i] < num[q[-1]]:
                q.pop()
            q.append(i)
        ans = str(num[q[0]])
        q.popleft()
        for i in range(k + 1, len(num)):
            while q and num[i] < num[q[-1]]:
                q.pop()
            q.append(i)
            ans += str(num[q[0]])
            q.popleft()
        return str(int(ans))