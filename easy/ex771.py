class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum = 0
        for i in range(len(S)):
            if S[i] in J:
                sum += 1
        return sum
