# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        graph = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            flag = True
            for j in range(n):
                if i != j:
                    if graph[i][j] == -1:
                        graph[i][j] = knows(i, j)
                    if graph[i][j]:
                        flag = False
                        break
                    if graph[j][i] == -1:
                        graph[j][i] = knows(j, i)
                    if not graph[j][i]:
                        flag = False
                        break
            if flag:
                return i
        return -1