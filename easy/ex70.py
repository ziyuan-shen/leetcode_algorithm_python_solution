class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        max_2 = n // 2
        num = 0
        def factorial(n):
            if n==0:
                return 1
            product = 1
            for i in range(1, n+1):
                product *= i
            return product
        for num_2 in range(1, max_2+1):
            position = n - num_2
            num += (factorial(position) / factorial(position - num_2) / factorial(num_2))
        return int(num + 1)