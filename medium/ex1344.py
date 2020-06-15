class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 360 * minutes / 60
        hour_angle = (hour % 12 / 12) * 360 + 30 * minutes / 60
        angle = abs(minute_angle - hour_angle)
        return min(angle, 360 - angle)