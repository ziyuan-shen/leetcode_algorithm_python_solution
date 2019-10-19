class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        int1 = 0
        int2 = 0
        for i in range(len(num1)):
            int1 = int1 * 10 + int(num1[i])
        for i in range(len(num2)):
            int2 = int2 * 10 + int(num2[i])
        return str(int1 + int2)
        