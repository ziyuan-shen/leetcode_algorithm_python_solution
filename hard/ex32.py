class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        idx = 0
        stack = []
        length = 0
        valid_start = 0
        while idx < len(s):
            if s[idx] == '(':
                stack.append(idx)
            else:
                if stack:
                    stack.pop(-1)
                    if stack:
                        length = idx - stack[-1]
                    else:
                        length = idx - valid_start + 1
                    if length > ans:
                        ans = length
                else:
                    valid_start = idx + 1
            idx += 1
        return ans