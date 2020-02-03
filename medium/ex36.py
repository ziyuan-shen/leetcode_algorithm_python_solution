class Solution:
    def checkNums(self, nums):
        nums = list(filter(lambda x: x != ".", nums))
        return len(set(nums)) == len(nums)
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            if not self.checkNums(board[row]):
                return False
        for col in range(9):
            if not self.checkNums([board[row][col] for row in range(9)]):
                return False
        for row in {0, 3, 6}:
            for col in {0, 3, 6}:
                nums = []
                for r in range(row, row+3):
                    nums += board[r][col:col+3]
                if not self.checkNums(nums):
                    return False
        return True