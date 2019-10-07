class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sub = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        number = 0
        for idx, i in enumerate(s):
            if i in sub and idx < len(s) - 1:
                if s[idx+1] in sub[i]:
                    number -= dic[i]
                else:
                    number += dic[i]
            else:
                number += dic[i]
        return number
            