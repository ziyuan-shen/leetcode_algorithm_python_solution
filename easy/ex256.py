class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        if len(costs) == 1:
            return min(costs[0])
        for i in range(1, len(costs)):
            for j in [0, 1, 2]:
                costs[i][j] = min(costs[i-1][(j+1)%3], costs[i-1][(j+2)%3]) + costs[i][j]
        return min(costs[-1])