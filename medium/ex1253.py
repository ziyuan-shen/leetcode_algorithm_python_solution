class Solution:       
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        matrix = [[0 for _ in range(len(colsum))], [0 for _ in range(len(colsum))]]
        for col in range(len(colsum)):
            if colsum[col] == 2:
                if upper == 0 or lower == 0:
                    return []
                matrix[0][col], matrix[1][col] = 1, 1
                upper -= 1
                lower -= 1
        for col in range(len(colsum)):
            if colsum[col] == 1:
                if upper > 0:
                    matrix[0][col] = 1
                    upper -= 1
                    continue
                if lower > 0:
                    matrix[1][col] = 1
                    lower -= 1
                    continue
                return []
        if upper != 0 or lower != 0:
            return []
        return matrix