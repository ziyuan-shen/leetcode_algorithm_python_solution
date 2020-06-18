from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        busset = {idx: set(route) for idx, route in enumerate(routes)}
        graph = defaultdict(set)
        for route in busset:
            if S in busset[route] and T in busset[route]:
                if S == T:
                    return 0
                else:
                    return 1
        for i in range(len(routes)):
            for j in range(len(routes)):
                if i != j:
                    for stop in routes[i]:
                        if stop in busset[j]:
                            graph[i].add(j)
                            break
        visited = set()
        target_routes = set()
        for route in busset:
            if S in busset[route]:
                visited.add(route)
            if T in busset[route]:
                target_routes.add(route)
        q = [(0, route) for route in visited]
        while q:
            level, route = q.pop(0)
            for neighbor in graph[route]:
                if neighbor not in visited:
                    if neighbor in target_routes:
                        return level + 2
                    visited.add(neighbor)
                    q.append((level + 1, neighbor))
        return -1