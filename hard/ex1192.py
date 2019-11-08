class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = {i: [] for i in range(n)}
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        current_id = 0
        visited = [False] * n
        id_list = [0] * n
        low_link = [0] * n
        bridges = []
        self.dfs(0, -1, graph, visited, current_id, id_list, low_link, bridges)
        return bridges
    
    def dfs(self, node, parent, graph, visited, current_id, id_list, low_link, bridges):
        visited[node] = True
        id_list[node] = current_id
        current_id += 1
        low_link[node] = id_list[node]
        for next_node in graph[node]:
            if next_node == parent:
                continue
            elif visited[next_node]:
                low_link[node] = min(low_link[node], low_link[next_node])
            else:
                self.dfs(next_node, node, graph, visited, current_id, id_list, low_link, bridges)
                low_link[node] = min(low_link[node], low_link[next_node])
                if id_list[node]<low_link[next_node]:
                    bridges.append([node, next_node])