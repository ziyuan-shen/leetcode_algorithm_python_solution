class Solution:
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
    
    def lcm(self, a, b):
        return a * b / self.gcd(a, b)
    
    def fractionAddition(self, expression: str) -> str:
        idx = 0
        signs = []
        nums = []
        if expression[0] == "-":
            signs.append(-1)
            idx += 1
        else:
            signs.append(1)
        while idx < len(expression):
            if expression[idx] == "+":
                signs.append(1)
                idx += 1
            elif expression[idx] == "-":
                signs.append(-1)
                idx += 1
            num = ""
            while idx < len(expression) and expression[idx] != "+" and expression[idx] != "-":
                num += expression[idx]
                idx += 1
            num = num.split("/")
            nums.append([int(num[0]), int(num[1])])
        cm = 1
        for num in nums:
            cm = self.lcm(num[1], cm)
        for num in nums:
            num[0] *= (cm / num[1])
        numerator = sum([signs[i] * nums[i][0] for i in range(len(nums))])
        if numerator < 0:
            sign = -1
            numerator = (-numerator)
        else:
            sign = 1
        cd = self.gcd(numerator, cm)
        return str(int(sign * numerator / cd)) + "/" + str(int(cm / cd))