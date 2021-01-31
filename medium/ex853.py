class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        time = [(target - position[i]) / speed[i] for i in range(len(position))]
        cars = [(position[i], time[i]) for i in range(len(position))]
        cars.sort(reverse = True)
        fleets = [cars[0][1]]
        for pos, time in cars[1:]:
            if time <= fleets[-1]:
                continue
            else:
                fleets.append(time)
        return len(fleets)