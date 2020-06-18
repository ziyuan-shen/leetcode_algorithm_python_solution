class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        length = len(maze)
        width = len(maze[0])
        q = [(start[0], start[1])]
        visited = {(start[0], start[1])}
        while q:
            x, y = q.pop(0)
            for idx, nei in enumerate([(x+1, y), (x-1, y), (x, y-1), (x, y+1)]):
                if nei[0] >= 0 and nei[0] < length and nei[1] >= 0 and nei[1] < width and maze[nei[0]][nei[1]] == 0:
                    if idx == 0:
                        new_x = x + 1
                        while new_x + 1 < length and maze[new_x+1][y] == 0:
                            new_x += 1
                        new_y = y
                    elif idx == 1:
                        new_x = x - 1
                        while new_x - 1 >= 0 and maze[new_x-1][y] == 0:
                            new_x -= 1
                        new_y = y
                    elif idx == 2:
                        new_y = y - 1
                        while new_y - 1 >= 0 and maze[x][new_y-1] == 0:
                            new_y -= 1
                        new_x = x
                    else:
                        new_y = y + 1
                        while new_y + 1 < width and maze[x][new_y+1] == 0:
                            new_y += 1
                        new_x = x
                    if new_x == destination[0] and new_y == destination[1]:
                        return True
                    if (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        q.append((new_x, new_y))
        return False