class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = 0
        for i in range(len(s)):
            if stack:
                if s[i] == stack[-1][0]:
                    count += 1
                else:
                    count = 1
                stack.append((s[i], count))
                if count == k:
                    for _ in range(k):
                        stack.pop()
                    if stack:
                        count = stack[-1][1]
                    else:
                        count = 0
            else:
                stack.append((s[i], 1))
                count = 1
        stack = [t[0] for t in stack]
        return "".join(stack)