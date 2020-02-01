class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            new_gas = gas[i:] + gas[:i]
            new_cost = cost[i:] + cost[:i]
            fuel = 0
            for j in range(len(gas)):
                fuel += new_gas[j]
                fuel -= new_cost[j]
                if fuel < 0:
                    break
            if fuel >= 0:
                return i
        return -1