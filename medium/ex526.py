class Solution:
    def calculate(self, pos, N, visited):
        for i in range(N):
            if not visited[i]:
                if pos % (i+1) == 0 or (i+1) % pos == 0:
                    visited[i] = True
                    if pos == N:
                        self.ans += 1
                    else:
                        self.calculate(pos + 1, N, visited)
                    visited[i] = False
                    
    def countArrangement(self, N: int) -> int:
        visited = [False for _ in range(N)]
        self.ans = 0
        self.calculate(1, N, visited)
        return self.ans