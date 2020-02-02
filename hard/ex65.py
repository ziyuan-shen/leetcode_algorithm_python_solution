class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        e_count = 0
        dot_count = 0
        for char in s:
            if not char.isdigit() and char not in {"e", ".", "+", "-"}:
                return False
            if char == "e":
                e_count += 1
                if e_count > 1:
                    return False
            if char == ".":
                dot_count += 1
                if dot_count > 1:
                    return False
        if e_count == 0:
            if s[0] == "-" or s[0] == "+":
                if len(s) < 2 or s[1] in {"+", "-"}:
                    return False
                s = s[1:]
            s = s.replace(".", "")
            return s.isdigit()
        else:
            nums = s.split("e")
            return "." not in nums[1] and self.isNumber(nums[0]) and self.isNumber(nums[1])