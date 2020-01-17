class Solution:
    def myAtoi(self, str: str) -> int:
        idx = 0
        while idx < len(str) and str[idx] == " ":
            idx += 1
        if idx >= len(str):
            return 0
        sign = 1
        if str[idx] == "-":
            sign = -1
            idx += 1
        elif str[idx] == "+":
            idx += 1
        if idx >= len(str):
            return 0
        num = ""
        while idx < len(str) and str[idx].isdigit():
            num += str[idx]
            idx += 1
        if not num:
            return 0
        num = sign * int(num)
        num = max(num, -2 ** 31)
        num = min(num, 2 ** 31 - 1)
        return num