class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        up, left = 0, 0
        while True:
            for i in instructions:
                if i == "L":
                    direction = (direction + 3) % 4
                elif i == "R":
                    direction = (direction + 1) % 4
                else:
                    if direction == 0:
                        up += 1
                    elif direction == 1:
                        left -= 1
                    elif direction == 2:
                        up -= 1
                    else:
                        left += 1
            if direction == 0:
                break
        return up == 0 and left == 0