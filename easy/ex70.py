class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            prev2_step = 1
            prev_step = 2
            for i in range(3, n + 1):
                current_step = prev2_step + prev_step
                prev2_step = prev_step
                prev_step = current_step
            return current_step