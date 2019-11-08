class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        node_stack = [0]
        visited_nodes = [0]
        id_dic = {0: 0}
        current_id = 0
        directed_connections = []
        while len(node_stack)>0:
            current_node = node_stack[-1]
            find_node_flag = False
            for path in connections:
                if path[0]==current_node or path[1]==current_node:
                    if path[0]==current_node:
                        connected_node = path[1]
                    else:
                        connected_node = path[0]
                    if connected_node not in visited_nodes:
                        visited_nodes.append(connected_node)
                        node_stack.append(connected_node)
                        current_id += 1
                        id_dic[connected_node] = current_id
                        directed_connections.append([current_node, connected_node])
                        find_node_flag = True
                        break
            if not find_node_flag:
                node_stack.pop()
        for path in connections:
            if not (path in directed_connections or path[::-1] in directed_connections):
                if id_dic[path[0]] < id_dic[path[1]]:
                    path = path[::-1]
                directed_connections.append(path)
        low_link_dic = {i: id_dic[i] for i in range(n)}
        for i in range(n):
            connected_nodes = [i]
            node_stack = [i]
            while len(node_stack) > 0:
                add_node_flag = False
                current_node = node_stack[-1]
                for path in directed_connections:
                    if path[0]==current_node and path[1] not in connected_nodes:
                        connected_nodes.append(path[1])
                        node_stack.append(path[1])
                        add_node_flag = True
                        break
                if not add_node_flag:
                    node_stack.pop()
            low_link_dic[i] = min([id_dic[j] for j in connected_nodes])
        bridges = []
        for path in directed_connections:
            if id_dic[path[0]] < low_link_dic[path[1]]:
                bridges.append(path)
        return bridges