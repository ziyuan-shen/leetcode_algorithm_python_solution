class Solution:
    def removeDuplicates(self, S: str) -> str:
        def remove(s):
            i = 0
            while (i+1)<len(s):
                if s[i] == s[i+1]:
                    s = s[:i] + s[i+2:]
                else:
                    i += 1
            return s
        while True:
            S_new = remove(S)
            if S_new == S:
                return S
            S = S_new