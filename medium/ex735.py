class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        idx = 0
        while idx + 1 < len(asteroids):
            a1 = asteroids[idx]
            a2 = asteroids[idx+1]
            if a1 > 0 and a2 < 0:
                if a1 + a2 == 0:
                    del asteroids[idx:idx+2]
                elif a1 + a2 > 0:
                    del asteroids[idx+1]
                else:
                    del asteroids[idx]
                idx = 0
            else:
                idx += 1
        return asteroids