class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = len(digits) - 1
        while True:
            if p >= 0:
                if digits[p] < 9:
                    digits[p] += 1
                    break
                else:
                    digits[p] = 0
                    p -= 1
            else:
                digits.insert(0, 1)
                break
        return digits