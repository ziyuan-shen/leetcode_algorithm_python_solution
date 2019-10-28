class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row_length = len(image)
        column_length = len(image[0])
        def node_in_image(node):
            return node[0] >= 0 and node[0] < row_length and node[1] >=0 and node[1] < column_length
        def add_node(node):
            row = node[0]
            column = node[1]
            connected_nodes = [[row-1, column], [row+1, column], [row, column-1], [row, column+1]]
            for item in connected_nodes:
                if node_in_image(item) and (not item in node_list):
                    if image[item[0]][item[1]] == source_color:
                        node_list.append(item)
                        add_node(item)
        source_color = image[sr][sc]
        node_list = [[sr, sc]]
        add_node([sr, sc])
        for node in node_list:
            image[node[0]][node[1]] = newColor
        return image