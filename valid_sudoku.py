from typing import List

class Solution:
    def validate_options(self, list_of_chars):
        dots = list_of_chars.count('.')
        choices = set(list_of_chars)
        if len(choices) + dots != len(list_of_chars):
            return False
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.validate_options(row):
                return False
        
        for index, value in enumerate(board):
            x = []
            for row in board:
                x.append(row[index])
            if not self.validate_options(x):
                return False