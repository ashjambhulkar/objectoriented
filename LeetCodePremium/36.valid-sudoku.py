#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [{} for i in range(9)], [{} for i in range(9)], [
            {} for i in range(9)]

        for i in range(9):
          for j in range(9):
            if board[i][j] != ".":
              val = int(board[i][j])
              box_id = (i//3)*3+j//3
              rows[i][val] = rows[i].get(val, 0) + 1
              cols[j][val] = cols[j].get(val, 0) + 1
              boxes[box_id][val] = boxes[box_id].get(val, 0) + 1

              if rows[i][val] > 1 or cols[j][val] > 1 or boxes[box_id][val] > 1:
                return False
        return True
        
# @lc code=end

