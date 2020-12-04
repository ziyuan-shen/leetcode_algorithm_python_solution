class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        bulbs = [0 for _ in range(len(light))]
        bluenum = 0
        ans = 0
        for idx, li in enumerate(light):
            if li == 1 or bulbs[li - 2] == 2:
                bulbs[li - 1] = 2
                bluenum += 1
                p = li
                while p < len(bulbs) and bulbs[p] == 1:
                    bulbs[p] = 2
                    bluenum += 1
                    p += 1
            else:
                bulbs[li - 1] = 1
            if bluenum == idx + 1:
                ans += 1
        return ans