class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends or target in deadends:
            return -1
        if target == "0000":
            return 0
        q = [(0, "0000")]
        visited = {"0000"}
        while q:
            level, code = q.pop(0)
            neighbors = []
            for i in range(4):
                up = str((int(code[i]) + 1) % 10)
                if code[i] == "0":
                    down = "9"
                else:
                    down = str(int(code[i]) - 1)
                neighbors.append(code[:i] + up + code[i+1:])
                neighbors.append(code[:i] + down + code[i+1:])
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in deadends:
                    if neighbor == target:
                        return level + 1
                    visited.add(neighbor)
                    q.append((level+1, neighbor))
        return -1