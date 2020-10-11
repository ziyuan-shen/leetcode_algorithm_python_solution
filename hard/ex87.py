from collections import deque
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        q = deque([[s1]])
        while q:
            strings = q.popleft()
            if "".join(strings) == s2:
                return True
            if len(strings) == len(s1):
                continue
            prevlen = 0
            for i in range(len(strings)):
                if len(strings[i]) == 1:
                    prevlen += 1
                else:
                    for j in range(len(strings[i]) - 1):
                        left = strings[i][:j+1]
                        right = strings[i][j+1:]
                        if not ((len(left) == 1 and left != s2[prevlen]) or (len(right) == 1 and right != s2[prevlen + len(left)])):
                            q.append(strings[:i] + [left, right] + strings[i+1:])
                        if not ((len(left) == 1 and left != s2[prevlen + len(right)]) or (len(right) == 1 and right != s2[prevlen])):
                            q.append(strings[:i] + [right, left] + strings[i+1:])
                    prevlen += len(strings[i])
        return False