class Solution:
    def validIPAddress(self, IP: str) -> str:
        if "." in IP:
            nums = IP.split(".")
            if len(nums) != 4:
                return "Neither"
            for num in nums:
                if not num.isdigit():
                    return "Neither"
                if len(str(int(num))) != len(num):
                    return "Neither"
                if int(num) > 255:
                    return "Neither"
            return "IPv4"
        elif ":" in IP:
            nums = IP.split(":")
            if len(nums) != 8:
                return "Neither"
            for num in nums:
                if len(num) > 4:
                    return "Neither"
                if not num.isalnum():
                    return "Neither"
                for char in num:
                    if char.isalpha() and ((ord(char) > 70 and ord(char) < 97) or ord(char) > 102):
                        return "Neither"
            return "IPv6"
        else:
            return "Neither"