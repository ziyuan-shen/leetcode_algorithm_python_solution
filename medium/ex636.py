class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0 for _ in range(n)]
        q = []
        for log in logs:
            function, startend, timestamp = tuple(log.split(":"))
            function = int(function)
            timestamp = int(timestamp)
            se = 1 if startend == "start" else 2
            q.append((timestamp, se, function))
        q.sort()
        time = q[0][0]
        stack = [q[0][2]]
        for i in range(1, len(q)):
            if q[i][1] == 1:
                if stack:
                    ans[stack[-1]] += q[i][0] - time
                stack.append(q[i][2])
                time = q[i][0]
            else:
                stack.pop()
                ans[q[i][2]] += (q[i][0] - time + 1)
                time = q[i][0] + 1
        return ans