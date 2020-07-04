class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parentdic = {}
        for i in range(m):
            for j in range(n):
                parentdic[(i, j)] = -1
        ans = []
        islands = {}
        for pos in positions:
            pos = (pos[0], pos[1])
            islands[pos] = {pos}
            parentdic[pos] = pos
            for neighbor in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
                if neighbor[0] >= 0 and neighbor[0] < m and neighbor[1] >= 0 and neighbor[1] < n:
                    if parentdic[neighbor] != -1 and parentdic[neighbor] != pos:
                        islands[pos] = islands[pos].union(islands[parentdic[neighbor]])
                        pre_islands = islands.pop(parentdic[neighbor])
                        for i in pre_islands:
                            parentdic[i] = pos
            ans.append(len(islands))
        return ans