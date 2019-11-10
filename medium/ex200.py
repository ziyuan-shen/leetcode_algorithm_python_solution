class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_num = len(grid)
        if row_num == 0:
            return 0
        col_num = len(grid[0])
        current_island_id = 1
        island_id = [[0]*col_num for i in range(row_num)]
        change_flag = True
        while change_flag:
            change_flag = False
            for i in range(row_num):
                for j in range(col_num):
                    if grid[i][j] == '1':
                        connected_lands = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
                        for land in connected_lands:
                            if land[0]>=0 and land[0]<row_num and land[1]>=0 and land[1]<col_num:
                                if grid[land[0]][land[1]] == '1' and island_id[land[0]][land[1]]>island_id[i][j]:
                                    island_id[i][j] = island_id[land[0]][land[1]]
                                    change_flag = True
                        if island_id[i][j] == 0:
                            island_id[i][j] = current_island_id
                            current_island_id += 1
                            change_flag = True
        ids = []
        for i in range(row_num):
            for j in range(col_num):
                if island_id[i][j] != 0:
                    ids.append(island_id[i][j])
        return len(set(ids))