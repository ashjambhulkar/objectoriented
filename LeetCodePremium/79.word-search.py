#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, row, col, count):
        if count == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[count]:
            return 
        temp = board[row][col]
        board[row][col] = ""

        result = self.dfs(board, word, row+1, col, count +
                          1) or self.dfs(board, word, row-1, col, count+1) or self.dfs(board, word, row, col+1, count+1) or self.dfs(board, word, row, col-1, count+1)

        board[row][col] = temp
        return result

        

                    
# @lc code=end
