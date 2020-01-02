class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow = len(board)
        ncol = len(board[0])
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] != word[0]:
                    continue
                visited = [[i, j]]
                idx = 1
                fail = {k: [] for k in range(len(word))}
                while idx < len(word):
                    start = visited[idx-1]
                    neighbors = [[start[0]-1, start[1]], [start[0]+1, start[1]], [start[0], start[1]-1], [start[0], start[1]+1]]
                    flag = False
                    for n in neighbors:
                        if n[0] >= 0 and n[0] < nrow and n[1] >= 0 and n[1] < ncol:
                            if board[n[0]][n[1]] == word[idx] and n not in visited and n not in fail[idx]:
                                visited.append(n)
                                idx += 1
                                flag = True
                                break
                    if not flag:
                        fail[idx-1].append(start)
                        visited.pop(-1)
                        idx -= 1
                        if idx == 0:
                            break
                if idx != 0:
                    return True
        return False
                        