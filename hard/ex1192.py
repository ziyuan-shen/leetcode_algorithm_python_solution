class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        def isConnected(connections):
            visited_dic = {i: 0 for i in range(n)}
            node_stack = [0]
            while len(node_stack) > 0:
                current_node = node_stack[-1]
                add_node_flag = False
                for path in connections:
                    if path[0] == current_node or path[1] == current_node:
                        if path[0] == current_node:
                            connected_node = path[1]
                        else:
                            connected_node = path[0]
                        if visited_dic[connected_node]==0:
                            visited_dic[connected_node] = 1
                            current_node = connected_node
                            node_stack.append(current_node)
                            add_node_flag = True
                            break
                if add_node_flag:
                    continue
                else:
                    node_stack.pop()
            return sum(visited_dic.values()) == n
        critical_connections = []
        for path in connections:
            connections_copy = connections[:]
            connections_copy.remove(path)
            if not isConnected(connections_copy):
                critical_connections.append(path)
        return critical_connections