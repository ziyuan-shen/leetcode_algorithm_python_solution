class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        self.ans = ''
        idx = 0
        i = 0
        left_idx = -1
        while i < len(S):
            if S[i] == '(':
                idx += 1
                if left_idx == -1:
                    left_idx = i
            if S[i] == ')':
                idx -= 1
            if (idx == 0) and (left_idx != -1):
                sub_str = S[left_idx+1:i]
                self.ans = self.ans + sub_str
                left_idx = -1
            i += 1
        return self.ans
