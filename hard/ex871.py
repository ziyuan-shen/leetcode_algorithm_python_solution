class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if len(stations) == 0:
            if startFuel >= target:
                return 0
            else:
                return -1
        else:
            if startFuel < stations[0][0]:
                return -1
            else:
                norefuel = self.minRefuelStops(target - stations[0][0], startFuel - stations[0][0], [[s[0] - stations[0][0], s[1]] for s in stations[1:]])
                refuel = self.minRefuelStops(target - stations[0][0], startFuel + stations[0][1] - stations[0][0], [[s[0] - stations[0][0], s[1]] for s in stations[1:]])
                if norefuel == -1 and refuel == -1:
                    return -1
                elif norefuel == -1:
                    return 1 + refuel
                else:
                    return min(norefuel, 1 + refuel)
                                                               