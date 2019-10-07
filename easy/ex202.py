class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            sum = 0
            while True:
                num, digit = num // 10, num % 10
                sum += digit ** 2
                if num == 0:
                    break
            return sum
        if n == 1:
            return True
        num_list = [n]
        next_num = n
        while True:
            next_num = sum_of_squares(next_num)
            if next_num == 1:
                return True
            if next_num in num_list:
                return False
            else:
                num_list.append(next_num)
        