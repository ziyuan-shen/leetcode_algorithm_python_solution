class Solution:
    def lastRemaining(self, n: int) -> int:
        first = 1
        interval = 1
        direction = "left"
        while n > 1:
            if direction == "left":
                first += interval
                n //= 2
                interval *= 2
                direction = "right"
            else:
                if n % 2 == 1:
                    first += interval
                n //= 2
                interval *= 2
                direction = "left"
        return first