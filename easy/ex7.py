class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        sign = 1 if x>=0 else -1
        x *= sign
        return_value = 0
        while True:
            x, digit = x // 10, x % 10
            return_value = return_value * 10 + digit
            if x == 0:
                break
        return_value *= sign
        if return_value < -2**31 or return_value > 2**31 - 1:
            return_value=0
        return return_value
        