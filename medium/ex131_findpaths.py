def findPaths(graph, s, d):
    paths = []
    path = [s]
    visited = {node: False for node in graph}
    visited[s] = True
    def dfs(visited, path):
        for neighbor in graph[path[-1]]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                if neighbor == d:
                    paths.append(path.copy())
                else:
                    dfs(visited, path)
                path.pop()
                visited[neighbor] = False
    dfs(visited, path)
    return paths

print(findPaths({0: [1, 2, 3], 1: [3], 2: [0, 1], 3: []}, 2, 3))