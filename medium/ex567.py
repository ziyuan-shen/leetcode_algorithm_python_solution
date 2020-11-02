from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])
        flag = True
        for char in c1:
            if char not in c2 or c1[char] != c2[char]:
                flag = False
                break
        if flag:
            return True
        for i in range(len(s1), len(s2)):
            c2[s2[i - len(s1)]] -= 1
            if s2[i] in c2:
                c2[s2[i]] += 1
            else:
                c2[s2[i]] = 1
            flag = True
            for char in c1:
                if char not in c2 or c1[char] != c2[char]:
                    flag = False
                    break
            if flag:
                return True
        return False